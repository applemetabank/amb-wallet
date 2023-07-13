export type Chain = {
    chainId: string;
    name: string;
    blockExplorerUrl: string;
    rpcUrl: string;
  };
  
export const goerli: Chain = {
    chainId: '5',
    name: 'Goerli',
    blockExplorerUrl: 'https://goerli.etherscan.io',
    rpcUrl: 'https://goerli.infura.io/v3/2b459efa587a4081b9da7374299d48ec',
};

export const mainnet: Chain = {
    chainId: '1',
    name: 'Ethereum',
    blockExplorerUrl: 'https://etherscan.io',
    rpcUrl: 'https://mainnet.infura.io/v3/2b459efa587a4081b9da7374299d48ec',
};

export const CHAINS_CONFIG = {
    [goerli.chainId]: goerli,
    [mainnet.chainId]: mainnet,
};