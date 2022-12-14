// SPDX-License-Identifier: MIT

pragma solidity 0.8.14;

contract KhelManch {
    uint256 public testvariable = 0;
    uint256 public totalProfiles;
    uint256 public totalContentCreators;
    uint256 public contentId;

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
        totalProfiles = 0;
        totalContentCreators = 0;
        contentId = 0;
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

    function addContentCreator(
        string memory _name,
        string memory _description,
        string memory _profilepic
    ) public onlyOwner {
        playerToCreator[msg.sender] = creator(_name, _description, _profilepic);
    }

    function addPlayer(
        string memory _name,
        string memory _description,
        uint256 _age,
        string memory _gender,
        string memory _location,
        string memory _sport,
        string memory _profilepic
    ) public onlyOwner {
        totalProfiles = totalProfiles + 1;
        uint256 id = totalProfiles;
        playerIdToPlayer[id] = player(
            id,
            msg.sender,
            _name,
            _description,
            _age,
            _gender,
            _location,
            _sport,
            _profilepic
        );
    }

    function addContent(
        uint256 _playerId,
        string memory _name,
        string memory _file,
        string memory _sport
    ) public onlyOwner {
        contentId = contentId + 1;
        uint256 id = contentId;
        contentIdToContent[id] = content(
            msg.sender,
            _playerId,
            _name,
            _file,
            _sport
        );
    }

    function testContract() public {
        testvariable = testvariable + 1;
    }
}
