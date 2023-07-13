pragma solidity ^0.8.0;

import "@openzeppelin/contracts/token/ERC20/IERC20.sol";

contract LiquidityMining {
    address public owner;
    uint256 public programDuration;
    uint256 public rewardAmount;
    uint256 public minimumLiquidity;
    uint256 public startTime;
    mapping(address => uint256) public liquidityProvided;
    IERC20 public SHE;

    constructor(uint256 _programDuration, uint256 _rewardAmount, uint256 _minimumLiquidity, address _SHE) {
        owner = msg.sender;
        programDuration = _programDuration;
        rewardAmount = _rewardAmount;
        minimumLiquidity = _minimumLiquidity;
        SHE = IERC20(_SHE);
    }

    function startProgram() public {
        require(msg.sender == owner, "Only the owner can start the program");
        require(SHE.balanceOf(address(this)) >= rewardAmount, "Insufficient reward amount");
        startTime = block.timestamp;
    }

    function addLiquidity(uint256 _amount) public {
        require(block.timestamp < startTime + programDuration, "Program has ended");
        require(SHE.transferFrom(msg.sender, address(this), _amount), "Transfer failed");
        liquidityProvided[msg.sender] += _amount;
    }

    function claimReward() public {
        require(block.timestamp >= startTime + programDuration, "Program has not ended");
        require(liquidityProvided[msg.sender] >= minimumLiquidity, "Minimum liquidity not met");
        uint256 reward = (rewardAmount * liquidityProvided[msg.sender]) / SHE.balanceOf(address(this));
        require(SHE.transfer(msg.sender, reward), "Transfer failed");
        liquidityProvided[msg.sender] = 0;
    }
}