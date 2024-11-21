'''
Author: wang w1838978548@126.com
Date: 2024-09-05 10:55:01
LastEditors: wang w1838978548@126.com
LastEditTime: 2024-09-05 11:31:13
FilePath: \Automation\ecfp.py
Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
'''
from rdkit import Chem
from rdkit.Chem import Draw

# 输入SMILES字符串
def generate_ecfp(smiles):
    mol = Chem.MolFromSmiles(smiles)  # Create molecule object
    if mol is None:
        print("Failed to create molecule from SMILES")
        return None
    else:
        structure = Chem.Draw.MolToImage(mol)
        print(structure)
    # fp = AllChem.GetMorganFingerprint(mol, 2, 2)  # Generate ECFP
    # return fp
    
smiles = 'OC1=CC=C(C[C@H](N)C(N[C@@H](CC2=CC=CC=C2)C(N[C@@H](CC(C)C)C(O)=O)=O)=O)C=C1.NCC(NCC(N[C@@H](CC(C)C)C(O)=O)=O)=O.NCC(N[C@@H](CC(C)C)C(O)=O)=O.NCC(N[C@@H](CC3=CC=CC=C3)C(N[C@@H](CC(C)C)C(O)=O)=O)=O'  # Example SMILES string
fp = generate_ecfp(smiles)