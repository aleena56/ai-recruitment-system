import glob

from parsers.resume_parser import parse_resume, save_extracted_resume

def run_batch_processing():

    files = glob.glob("data/raw/*")

    for file_path in files:
        try:
            parsed = parse_resume(file_path)
            output = save_extracted_resume(parsed)

            print(f"Processed: {file_path}")
            print(f"Saved: {output}\n")

        except Exception as e:
            print(f"Failed: {file_path} - {e}")

if __name__ == "__main__":
    run_batch_processing()