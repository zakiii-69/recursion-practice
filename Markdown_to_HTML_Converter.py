import sys
import markdown

def convert_markdown_to_html(input_file, output_file):

    with open(input_file, encoding='utf-8') as f:
        text = f.read()

    html = markdown.markdown(text)

    with open(output_file, 'w',encoding='utf-8') as f:
        f.write(html)

def main():

    if len(sys.argv) != 4:
        print(f"Usage: python3 file_converter.py markdown inputfile outputfile")
        sys.exit(1)
    
    command = sys.argv[1]
    input_file = sys.argv[2]
    output_file = sys.argv[3]

    if command != "markdown":
        print(f"Error: Unknown command '{command}'")
        sys.exit(1)

    convert_markdown_to_html(input_file, output_file)
    print(f"Converted {input_file} to {output_file}")

if __name__ == "__main__":
    main()