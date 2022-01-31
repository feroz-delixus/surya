from flask import Flask, request, redirect, render_template
from flask_cors import CORS, cross_origin
from pathlib import Path
import os, sys, jenkins
import subprocess


api = Flask(__name__)
CORS(api, resources={r"/api/*": {"origins": "*"}})
api.config['CORS_HEADERS'] = 'Content-Type'


CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(CURRENT_DIR))


@api.errorhandler(Exception)
def handle_exception(error):
    return {'message': str(error)}, getattr(error, 'code', 500)


@api.route('/surya')
def rediret_to_surya_frontend():
    return redirect("13.126.95.15:5000/api/suryatool", code=302)


@api.route("/api/suryatool")
def index():
    return "Surya Parse Solidity - Root API call"

# http://localhost:5000/api/suryatool/parse?solidityFile=deposit_box.sol&basePath=/home/delixus/repos/mythril-scan/solidityFiles/sol0.8.0
@api.route('/api/suryatool/parse', methods=['GET'])
def parseSolidityFile():
    solidityFile = request.args.get('solidityFile')
    basePath = request.args.get('basePath')
    return_value = ''
    if solidityFile.endswith("*.sol"):
        for path in Path(basePath).iterdir():
            process = os.popen('surya parse ' + str(path))
            return_value += "\n" +  process.read()
    else:
        solidityFileName = basePath + "/" + solidityFile
        process = os.popen('surya parse ' + solidityFileName)
        return_value += "\n" +  process.read()

    return return_value


# http://localhost:5000/api/suryatool/describe?solidityFile=deposit_box.sol&basePath=/home/delixus/repos/mythril-scan/solidityFiles/sol0.8.0
@api.route('/api/suryatool/describe', methods=['GET'])
def describeSolidityFile():
    basePath = request.args.get('basePath')
    solidityFile = request.args.get('solidityFile')
    return_value = ''
    if solidityFile.endswith("*.sol"):
        for path in Path(basePath).iterdir():
            process = os.popen('surya describe ' + str(path))
            return_value += "\n" +   process.read()
    else:
        solidityFileName = basePath + "/" + solidityFile
        process = os.popen('surya describe ' + solidityFileName)
        return_value += "\n" +   process.read()

    return return_value


# http://localhost:5000/api/suryatool/graph?solidityFile=deposit_box.sol&basePath=/home/delixus/repos/mythril-scan/solidityFiles/sol0.8.0
@api.route('/api/suryatool/graph', methods=['GET'])
def graphSolidityFile():
    basePath = request.args.get('basePath')
    solidityFile = request.args.get('solidityFile')
    return_value = ''
    if solidityFile.endswith("*.sol"):
        for path in Path(basePath).iterdir():
            solidityFileName = str(path.name)
            solidityPngFile = basePath + '/' + solidityFileName.split('.')[0] + '_graph.png'
            return_value += "\n" +  os.system('surya graph ' + str(path) + " | dot -Tpng > " + solidityPngFile)
    else:
        solidityFileName = basePath + "/" + solidityFile
        pngFile = basePath + "/" + solidityFile.split('.')[0] + "_graph.png"
        return_value = os.system('surya graph ' + solidityFileName + " | dot -Tpng > " + pngFile)

    return "Graph Done"

# http://localhost:5000/api/suryatool/ftrace?solidityFile=deposit_box.sol&basePath=/home/delixus/repos/mythril-scan/solidityFiles/sol0.8.0
@api.route('/api/suryatool/ftrace', methods=['GET'])
def ftraceSolidityFile():
    basePath = request.args.get('basePath')
    solidityFile = request.args.get('solidityFile')
    return_value = ''
    if solidityFile.endswith("*.sol"):
        for path in Path(basePath).iterdir():
            solidityFileName = str(path.name)
            return_value += "\n" +  os.system('surya ftrace APMRegistry::_newRepo all ' + str(path))
    else:
        solidityFileName = basePath + "/" + solidityFile
        return_value += "\n" +  str(os.system('surya ftrace APMRegistry::_newRepo all ' + solidityFileName))

    return "Successfully ftrace done"


# http://localhost:5000/api/suryatool/flatten?solidityFile=deposit_box.sol&basePath=/home/delixus/repos/mythril-scan/solidityFiles/sol0.8.0
@api.route('/api/suryatool/flatten', methods=['GET'])
def flattenSolidityFile():
    basePath = request.args.get('basePath')
    solidityFile = request.args.get('solidityFile')
    return_value = ''
    if solidityFile.endswith("*.sol"):
        for path in Path(basePath).iterdir():
            process = os.popen('surya flatten ' + str(path))
            return_value += "\n" +  process.read()
    else:
        solidityFileName = basePath + "/" + solidityFile
        process = os.popen('surya flatten ' + solidityFileName)
        return_value += "\n" +  process.read()
    return return_value



# http://localhost:5000/api/suryatool/dependencies?solidityFile=deposit_box.sol&basePath=/home/delixus/repos/mythril-scan/solidityFiles/sol0.8.0
@api.route('/api/suryatool/dependencies', methods=['GET'])
def dependencisesSolidityFile():

    basePath = request.args.get('basePath')
    solidityFile = request.args.get('solidityFile')
    return_value = ''
    solidityFileName = ''
    if solidityFile.endswith("*.sol"):
        for path in Path(basePath).iterdir():
            solidityFileName = str(path.name)
            command = 'surya dependencies ' + solidityFileName.split('.')[0] + " " + str(path)
            return_value += subprocess.check_output(command, shell=True)
    else:
        solidityFileName = basePath + "/" + solidityFile
        command = 'surya dependencies ' + solidityFile.split('.')[0] + " " + solidityFileName
        return_value += subprocess.check_output(command, shell=True)

    return return_value



# http://localhost:5000/api/suryatool/mdreport?solidityFile=deposit_box.sol&basePath=/home/delixus/repos/mythril-scan/solidityFiles/sol0.8.0
@api.route('/api/suryatool/mdreport', methods=['GET'])
def mdreportSolidityFile():
    basePath = request.args.get('basePath')
    solidityFile = request.args.get('solidityFile')
    return_value = ''
    solidityFileName = ''
    if solidityFile.endswith("*.sol"):
        for path in Path(basePath).iterdir():
            solidityFileName = str(path.name)
            solidityMdFile = basePath + '/' + solidityFileName.split('.')[0] + '.md'
            command = 'surya mdreport ' + solidityMdFile + ' ' + str(path)
            subprocess.check_output(command, shell=True)
    else:
        solidityFileName = basePath + "/" + solidityFile
        solidityMdFile = basePath + "/" + solidityFile.split('.')[0] + '.md'
        command = 'surya mdreport ' + ' ' + solidityMdFile + ' ' + solidityFileName
        subprocess.check_output(command, shell=True)

    return "Successfully created the MdReport "



# http://localhost:5000/api/suryatool/inheritance?solidityFile=deposit_box.sol&basePath=/home/delixus/repos/mythril-scan/solidityFiles/sol0.8.0
@api.route('/api/suryatool/inheritance', methods=['GET'])
def inheritanceSolidityFile():
    basePath = request.args.get('basePath')
    solidityFile = request.args.get('solidityFile')
    return_value = ''
    if solidityFile.endswith("*.sol"):
       for path in Path(basePath).iterdir():
          solidityFileName = str(path.name)
          solidityPngFile = basePath + "/" + solidityFileName.split('.')[0] + '_inheritance.png'
          command = 'surya inheritance ' + str(path) + " | dot -Tpng > " + solidityPngFile
          os.system(command)
    else:
       solidityFileName = basePath + "/" + solidityFile
       solidityPngFile = basePath + "/" + solidityFile.split('.')[0] + '_inheritance.png'
       command = 'surya inheritance ' + solidityFileName + " | dot -Tpng > " + solidityPngFile
       os.system(command)

    return " inheritance png file is created "



if __name__ == '__main__':
    api.run(host='0.0.0.0', debug=True)
