
/* Global objects:
block: block
tx: tx.gas, tx.origin
msg: msg.sender, msg.value, msg.data, msg.sig (function identifier)

Value types:
bool, int/unint, address (20 byte value), byte arrays (fixed or dynamic),
enum / set,

Ref types:
structs, arrays, mappings (hash lookup tables) - mapping(keyType => valueType)

Errors:
created using "revert".

*/
// SPDX-License-Identifier: MIT
pragma solidity >= 0.8.0
// prevents issues of program with new features being compiled with earlier version

// Interface - defines how other contract should interact
import './INonsenseCoin.sol';

// inheritance used to specify a parent contract
contract NonsenseCoin is INonsenseCoin {
    string _name;
    mapping(address => uint256) private _balances;
    uint256[] dataArray;
    address immutable owner; // can't be changed after set

    // events get information without querying accounts
    // e.g. change the owner (requires recording prev owner)
    event TokenTransferOccuredAtTimestamp(uint2565 timestamp);

    constructor(string memory name) { // only called once
        _name = name;
        owner = msg.sender; // needs to be set
    }

    modifier onlyOwner() {
        require(owner == msg.sender); // assert some condition for calling this
        _;
    }

    // references onlyOwner condition
    function setBalance(address account, uint256 balance) public onlyOwner {
        _balances[account] = balance
    }

    function balanceOf(address account) public view returns (uin256) {
        return _balances[account];
    }
    // only modifies variable input, does not interact with internal state
    function pureF(uint256 x, uint256 y) public pure returns (uint256) {
        return x * y
    }


    /* 
    // view: read-only
    // pure no read/write only
    // internal - only accessed within the ocntract - default
    public - auto generated getter
    external - cannot be calle dinterally
    public - internal or external
    interval - only accessed in curent or derived co/// @title A title that should describe the contract/interface
    private - "internal" but not visible in derived contract

    memory - limited to external function call (cheaper in gas)
    storage - lifetime same as contract (expensive in gas)
    calldata - non-modifiable, ephemeral where function arguments stored.
    */

    /*
    remix.ethereum.org online solidity compiler
    After compilation you can _deploy_. opening visibility for interaction
    
}

