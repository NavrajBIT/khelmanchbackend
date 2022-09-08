// SPDX-License-Identifier: MIT
import "./login.sol";
import "./Content.sol";

pragma solidity 0.8.14;

contract Admin {
    PlatformLogin platformLogin;
    KhelManch khelManch;

    uint256 public ownerCount;
    mapping(address => uint256) public ownerToOwnerId;
    uint256 public blockedOwnerCount;
    mapping(address => uint256) public blockedOwnerToOwnerId;

    constructor(address _platformLogin, address _khelManch) {
        blockedOwnerCount = 0;
        ownerCount = 1;
        ownerToOwnerId[msg.sender] = ownerCount;
        platformLogin = PlatformLogin(_platformLogin);
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

    function addCreator(string memory _name, string memory _profilePic)
        public
        onlyOwner
    {
        platformLogin.addContentCreator(_name, _profilePic);
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
    ) public onlyOwner {
        khelManch.addProfile(
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
    }

    function uploadVideo(
        uint256 _profileId,
        string memory _videoLink,
        string memory _description,
        string memory _skillName
    ) public onlyOwner {
        khelManch.uploadVideo(_profileId, _videoLink, _description, _skillName);
    }
}
