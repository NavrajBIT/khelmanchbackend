// SPDX-License-Identifier: MIT

pragma solidity 0.8.14;

contract KhelManch {
    struct profile {
        uint256 profileId;
        address profileCreator;
        string name;
        uint256 age;
        string gender;
        string fatherName;
        string motherName;
        string Address;
        string imgHash;
        string skillName;
        string description;
    }

    struct videoContent {
        uint256 profileId;
        string videoLink;
        string description;
        string skillName;
    }

    uint256 public totalProfiles;

    mapping(uint256 => profile) public profileMapping; // mapping to get profile from Id
    mapping(address => uint256[]) public userPosts; // Array to store profiles(Id) done by user
    mapping(uint256 => videoContent) public videoContentMapping; //mapping to get video from Id

    uint256 public ownerCount;
    mapping(address => uint256) public ownerToOwnerId;
    uint256 public blockedOwnerCount;
    mapping(address => uint256) public blockedOwnerToOwnerId;

    constructor() {
        blockedOwnerCount = 0;
        ownerCount = 1;
        ownerToOwnerId[msg.sender] = ownerCount;
        totalProfiles = 0;
    }

    modifier onlyProfileAuthor(uint256 id) {
        require(
            msg.sender == profileMapping[id].profileCreator,
            "You are not Author!"
        );
        _;
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

    function addProfile(
        string memory _name,
        uint256 _age,
        string memory _gender,
        string memory _fatherName,
        string memory _motherName,
        string memory _address,
        string memory _imgHash,
        string memory _skillName,
        string memory _description
    ) public onlyOwner{
        totalProfiles = totalProfiles + 1;
        uint256 id = totalProfiles;
        profileMapping[id] = profile(
            id,
            msg.sender,
            _name,
            _age,
            _gender,
            _fatherName,
            _motherName,
            _address,
            _imgHash,
            _skillName,
            _description
        );

        userPosts[msg.sender].push(totalProfiles);
    }

    function uploadVideo(
        uint256 _profileId,
        string memory _videoLink,
        string memory _description,
        string memory _skillName
    ) public onlyOwner{
        videoContentMapping[_profileId] = videoContent(
            _profileId,
            _videoLink,
            _description,
            _skillName
        );
    }
}
