import subprocess
from pathlib import Path

def convert_docx_to_md(docx_path: Path):
    md_path = docx_path.with_suffix('.md')
    try:
        subprocess.run(['pandoc', str(docx_path), '-o', str(md_path)],
                       check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        print(f"✅ Конвертирован: {docx_path.name} → {md_path.name}")
    except subprocess.CalledProcessError as e:
        print(f"❌ Ошибка при конвертации {docx_path.name}:\n{e.stderr.decode()}")

def main():
    # Получаем список всех .docx файлов в текущей директории
    for docx_file in Path('.').glob('*.docx'):
        convert_docx_to_md(docx_file)

if __name__ == '__main__':
    main()

