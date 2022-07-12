// SPDX-License-Identifier:MIT
pragma solidity ^0.8.0;

contract WavePortal {
    mapping(address => uint256) public lastWavedAt;

    uint256 private seed;
    uint256 public totalWaves;

    event NewWave(address indexed _from, uint256 timestamp, string _message);

    struct Wave {
        address waver;
        string message;
        uint256 timestamp;
    }

    Wave[] public waves;

    constructor() payable {
        seed = (block.timestamp + block.difficulty) % 100;
    }

    function wave(string memory _message) public payable {
        //     require(
        //         lastWavedAt[msg.sender] + 15 seconds < block.timestamp,
        //         "Wait 15 seconds"
        //     );

        //     lastWavedAt[msg.sender] = block.timestamp;

        totalWaves += 1;

        waves.push(Wave(msg.sender, _message, block.timestamp));

        seed = (block.timestamp + block.difficulty + seed) % 100;

        if (seed <= 50) {
            uint256 prizeAmount = 0.0001 ether;
            require(
                prizeAmount <= address(this).balance,
                "Trying to withdraw more money than this contract has!!!"
            );

            (bool success, ) = payable(msg.sender).call{value: prizeAmount}("");

            require(success, "Failed to withdraw money from contract.");
        }

        emit NewWave(msg.sender, block.timestamp, _message);
    }

    function getAllWaves() public view returns (Wave[] memory) {
        return waves;
    }

    function getTotalWaves() public view returns (uint256) {
        return totalWaves;
    }

    function get_Balance() public view returns (uint256) {
        return address(this).balance;
    }
}
