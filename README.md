# delixus-surya-api-svc

Surya tool is found in the location https://github.com/ConsenSys/surya

Install the Surya tool by 

**npm install -g surya
**
Then run the requirements.txt

pip install -r requirements.txt

Then run the code 
**python suryarestcall.py **

The following are the API's currently available

/api/suryatool 
This is for going to the index of the API

Parse :-

http://13.126.95.15:5000/api/suryatool/parse?solidityFile=deposit_box.sol&basePath=/home/delixus/repos/mythril-scan/solidityFiles/sol0.8.0

This is for parsing the solidity file and get its response

Describe:-

http://13.126.95.15:5000/api/suryatool/describe?solidityFile=deposit_box.sol&basePath=/home/delixus/repos/mythril-scan/solidityFiles/sol0.8.0

This is for describing the solidity file

Graph :- 

http://13.126.95.15:5000/api/suryatool/graph?solidityFile=deposit_box.sol&basePath=/home/delixus/repos/mythril-scan/solidityFiles/sol0.8.0

This is for getting the graph

Ftrace:-  

http://13.126.95.15:5000/api/suryatool/ftrace?solidityFile=deposit_box.sol&basePath=/home/delixus/repos/mythril-scan/solidityFiles/sol0.8.0

This is for getting the ftrace

Flatten :- 

http://13.126.95.15:5000/api/suryatool/flatten?solidityFile=deposit_box.sol&basePath=/home/delixus/repos/mythril-scan/solidityFiles/sol0.8.0

This is for flattening the solidity file

Dependencies :-  

http://13.126.95.15:5000/api/suryatool/dependencies?solidityFile=deposit_box.sol&basePath=/home/delixus/repos/mythril-scan/solidityFiles/sol0.8.0

This is for finding the dependencies of the solidity file

MdReport :- 

http://13.126.95.15:5000/api/suryatool/mdreport?solidityFile=deposit_box.sol&basePath=/home/delixus/repos/mythril-scan/solidityFiles/sol0.8.0

This is for finding the MDreport , ie .md file of the solidity file which might give upto the address of the solidity file

Inheritance :- 

http://13.126.95.15:5000/api/suryatool/inheritance?solidityFile=deposit_box.sol&basePath=/home/delixus/repos/mythril-scan/solidityFiles/sol0.8.0

This is for finding the inheritance of the solidity files.


