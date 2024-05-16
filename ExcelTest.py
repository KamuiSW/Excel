import pandas as pd

def merge_and_replace(sheet_a_name, sheet_b_name, DateToCheck, OriginalToBeReplaced, BeingReplaced):
    # Read Excel sheits
    df_a = pd.read_excel('Sheet1.xlsx', sheet_name=None)
    df_b = pd.read_excel('Sheet2.xlsx', sheet_name=sheet_b_name)

    for index, row in df_b.iterrows():
        # check if datr matchaes with thing
        if row['date'] == DateToCheck:
            # Find nameeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee
            match = df_a[sheet_a_name].loc[df_a[sheet_a_name]['names'] == row['names']]
            if not match.empty and not pd.isna(row[OriginalToBeReplaced]):
                df_a[sheet_a_name].loc[match.index, BeingReplaced] = row[OriginalToBeReplaced]
                # Copy the THEM DATE
                df_a[sheet_a_name].loc[match.index, 'date'] = row['date']

    # Save the updated sheet
    with pd.ExcelWriter('Sheet1.xlsx') as writer:
        for sheet, df in df_a.items():
            df.to_excel(writer, sheet_name=sheet, index=False)

OriginalToBeReplaced = 'numbers'
DateToCheck = 'B'
BeingReplaced = 'numbers'
ShInOrg = 'Sheet1'
ShInNew = 'Sheet2'
merge_and_replace(ShInOrg, ShInNew, DateToCheck, OriginalToBeReplaced, BeingReplaced)
