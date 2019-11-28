web3 = new Web3(web3.currentProvider);
window.ethereum.enable();

// for test
var contractAddress = '0x7203a59116d8d001611fcec365377783945d6993';
//test = 0x679e69c8c69040090ae3e4b32639509212ec6128
var abi = [
	{
		"constant": false,
		"inputs": [
			{
				"internalType": "string",
				"name": "name",
				"type": "string"
			}
		],
		"name": "addCandidate",
		"outputs": [],
		"payable": false,
		"stateMutability": "nonpayable",
		"type": "function"
	},
	{
		"inputs": [],
		"payable": false,
		"stateMutability": "nonpayable",
		"type": "constructor"
	},
	{
		"constant": false,
		"inputs": [
			{
				"internalType": "uint8",
				"name": "_id",
				"type": "uint8"
			}
		],
		"name": "vote",
		"outputs": [],
		"payable": false,
		"stateMutability": "nonpayable",
		"type": "function"
	},
	{
		"anonymous": false,
		"inputs": [
			{
				"indexed": false,
				"internalType": "uint8",
				"name": "_id",
				"type": "uint8"
			},
			{
				"indexed": false,
				"internalType": "address",
				"name": "_voter",
				"type": "address"
			}
		],
		"name": "VotedEvent",
		"type": "event"
	},
	{
		"constant": true,
		"inputs": [
			{
				"internalType": "uint8",
				"name": "_id",
				"type": "uint8"
			}
		],
		"name": "getCandidate",
		"outputs": [
			{
				"internalType": "string",
				"name": "",
				"type": "string"
			},
			{
				"internalType": "uint8",
				"name": "",
				"type": "uint8"
			}
		],
		"payable": false,
		"stateMutability": "view",
		"type": "function"
	},
	{
		"constant": true,
		"inputs": [],
		"name": "getCandidateListLength",
		"outputs": [
			{
				"internalType": "uint256",
				"name": "",
				"type": "uint256"
			}
		],
		"payable": false,
		"stateMutability": "view",
		"type": "function"
	},
	{
		"constant": true,
		"inputs": [],
		"name": "getOwner",
		"outputs": [
			{
				"internalType": "address",
				"name": "",
				"type": "address"
			}
		],
		"payable": false,
		"stateMutability": "view",
		"type": "function"
	}
]

var votingInstance = web3.eth.contract(abi);
var Donggora = votingInstance.at(contractAddress);
var length;

function addCandidate(name) {
	Donggora.addCandidate(name, function () {

	});
}

function getCandidate() {
	var name;
	var count;
	//var length;
	//console.log("length ? " +length);
	/*Donggora.getCandidateListLength(function(err, length){
		for (var i = 0; i < length; i++) {
			//console.log("id : " + i);
			Donggora.getCandidate(i, function (err, result) {
				name = result[0];
				count = result[1];
				console.log("name : " + name);
				console.log("count : " + count);
			});
		}
	});*/
	Donggora.getCandidate(0, function (err, result) {
		name = result[0];
		count = result[1];
		console.log("name : " + name);
		console.log("count : " + count);
	});
}

/*function getCandidateListLength() {
	var length;
	Donggora.getCandidateListLength(function (err, result) {
		length = result;
		//console.log("length of list : " + length);
		//return length;
	});
	return length;
	//console.log("length of list : " + length);
}*/

function showTheResult() {
	var name;
	var max = 0;


	var obj = Donggora.getCandidateListLength(function(err, result){
		//console.log("length is " + result);
		length = result;
		for (var i=0;i<result;i++){
			//document.getElementById("test").innerHTML = result;
			
			Donggora.getCandidate(i, function(err, result){
				console.log("name : " + result[0]);
				console.log("count : " + result[1]);
			});
		}
	});
}

function vote(index) {
	Donggora.vote(index, function (err, result) {
		console.log(err);
	});
}