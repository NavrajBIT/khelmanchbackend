// SPDX-License-Identifier: MIT
import "./Content.sol";

pragma solidity 0.8.14;

contract Admin {
    KhelManch khelManch;

    uint256 public ownerCount;
    mapping(address => uint256) public ownerToOwnerId;
    uint256 public blockedOwnerCount;
    mapping(address => uint256) public blockedOwnerToOwnerId;

    constructor(address _khelManch) {
        blockedOwnerCount = 0;
        ownerCount = 1;
        ownerToOwnerId[msg.sender] = ownerCount;
        khelManch = KhelManch(_khelManch);
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

    function addCreator(
        string memory _name,
        string memory _description,
        string memory _profilePic
    ) public onlyOwner {
        khelManch.addContentCreator(_name, _description, _profilePic);
    }

    function addProfile(
        string memory _name,
        string memory _description,
        uint256 _age,
        string memory _gender,
        string memory _location,
        string memory _sport,
        string memory _profilepic
    ) public onlyOwner {
        khelManch.addPlayer(
            _name,
            _description,
            _age,
            _gender,
            _location,
            _sport,
            _profilepic
        );
    }

    function uploadContent(
        uint256 _playerId,
        string memory _name,
        string memory _file,
        string memory _sport
    ) public onlyOwner {
        khelManch.addContent(_playerId, _name, _file, _sport);
    }
}
