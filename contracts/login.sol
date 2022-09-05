// SPDX-License-Identifier: MIT

pragma solidity 0.8.14;

contract PlatformLogin {
    struct creator {
        uint256 id;
        address ethAddress;
        string usernames;
        string profilePic;
    }

    uint256 public totalContentCreators;

    mapping(address => creator) public addressToUser;

    uint256 public ownerCount;
    mapping(address => uint256) public ownerToOwnerId;
    uint256 public blockedOwnerCount;
    mapping(address => uint256) public blockedOwnerToOwnerId;

    constructor() {
        blockedOwnerCount = 0;
        ownerCount = 1;
        ownerToOwnerId[msg.sender] = ownerCount;
        totalContentCreators = 0;
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

    event logRegisterContentCreator(address user, uint256 id);

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

    function addContentCreator(string memory _name, string memory _profilePic)
        public
        onlyOwner
    {
        totalContentCreators = totalContentCreators + 1;
        uint256 id = totalContentCreators;
        addressToUser[msg.sender] = creator(id, msg.sender, _name, _profilePic);
        emit logRegisterContentCreator(msg.sender, totalContentCreators);
    }
}
