// SPDX-License-Identifier: MIT

pragma solidity 0.8.14;

contract KhelManch {
    uint256 public testvariable = 0;
    struct creator {
        string name;
        string description;
        string profilepic;
    }

    struct player {
        uint256 playerId;
        address profileCreator;
        string name;
        string description;
        uint256 age;
        string gender;
        string location;
        string sport;
        string profilepic;
    }

    struct content {
        address creator;
        uint256 playerId;
        string name;
        string file;
        string sport;
    }

    mapping(address => creator) public playerToCreator;
    mapping(uint256 => player) public playerIdToPlayer;
    mapping(uint256 => content) public contentIdToContent;

    uint256 public ownerCount;
    mapping(address => uint256) public ownerToOwnerId;
    uint256 public blockedOwnerCount;
    mapping(address => uint256) public blockedOwnerToOwnerId;

    constructor() {
        blockedOwnerCount = 0;
        ownerCount = 1;
        ownerToOwnerId[msg.sender] = ownerCount;
    }

    modifier onlyOwner() {
        require(
            ownerToOwnerId[msg.sender] > 0,
            "Only owner can call this function."
        );
        require(
            blockedOwnerToOwnerId[msg.sender] == 0,
            "You have been blocked."
        );
        _;
    }

    function setOwner(address _newOwner) public onlyOwner {
        require(ownerToOwnerId[_newOwner] == 0, "Owner already added.");
        ownerCount = ownerCount + 1;
        ownerToOwnerId[_newOwner] = ownerCount;
    }

    function blockOwner(address _owner) external onlyOwner {
        require(msg.sender != _owner, "You cannot block yourself");
        blockedOwnerCount = blockedOwnerCount + 1;
        blockedOwnerToOwnerId[_owner] = blockedOwnerCount;
    }

    function testContract() public {
        testvariable = testvariable + 1;
    }
}
