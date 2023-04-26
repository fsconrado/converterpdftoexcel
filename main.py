import PyPDF4
import pandas as pd
import tabula

def extrair_tabelas_pdf(arquivo_pdf):
    tabelas = tabula.read_pdf(arquivo_pdf, pages='all', multiple_tables=True)
    return tabelas

def main():
    arquivo_pdf = '/pdf/arquivo.pdf'
    arquivo_excel = '/result_xls/path/arquivo.xlsx'

    tabelas = extrair_tabelas_pdf(arquivo_pdf)
    writer = pd.ExcelWriter(arquivo_excel, engine='openpyxl')

    for i, tabela in enumerate(tabelas):
        tabela.to_excel(writer, sheet_name=f'Tabela_{i+1}', index=False)

    writer.close()

if __name__ == '__main__':
    main()
