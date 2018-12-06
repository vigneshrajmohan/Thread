import appex, os, runpy

def main():
    py_file = appex.get_file_path()
    if not py_file or os.path.splitext(py_file)[1] != '.py':
        print('No Python file')
        return
    runpy.run_path(py_file)

if __name__ == '__main__':
    main()
