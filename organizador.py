import collections
import tkinter as tk
from tkinter import filedialog, scrolledtext
import time

def process_file(input_file):
    encodings = [
           'utf-8', 'iso-8859-1', 'ascii', 'utf-16', 'utf-32',
            'cp1252', 'macroman', 'big5', 'shift_jis', 'gb2312',
            'iso-8859-2', 'iso-8859-3', 'iso-8859-4', 'iso-8859-5',
            'iso-8859-6', 'iso-8859-7', 'iso-8859-8', 'iso-8859-9',
            'iso-8859-10', 'iso-8859-11', 'iso-8859-13', 'iso-8859-14',
            'iso-8859-15', 'iso-8859-16', 'koi8-r', 'koi8-u', 'cp437',
            'cp850', 'cp852', 'cp866', 'cp874', 'tis-620', 'windows-1250',
            'windows-1251', 'windows-1253', 'windows-1254', 'windows-1255',
            'windows-1256', 'windows-1257', 'windows-1258', 'maccentraleurope',
            'maciceland', 'macroman', 'maccroatian', 'macromania', 'macthai',
            'machebrew', 'macarabic', 'macgreek', 'macturkish', 'macukraine',
            'macintosh', 'iso-2022-jp', 'iso-2022-cn', 'iso-2022-kr', 'utf-7',
            'utf-1', 'utf-32be', 'utf-32le', 'utf-16be', 'utf-16le', 'gb18030',
            'hz', 'euc-jp', 'euc-jisx0213', 'euc-kr', 'euc-tw', 'gbk', 'gb2312-80',
            'cp037', 'cp424', 'cp500', 'cp737', 'cp775', 'cp857', 'cp860', 'cp861',
            'cp863', 'cp865', 'cp869', 'cp1026', 'cp1140', 'maclatin2', 'shift_jisx0213',
            'windows-874', 'windows-949', 'windows-936', 'windows-950', 'cp1258', 
            'utf-16-le', 'utf-16-be', 'utf-32-le', 'utf-32-be', 'cp850', 'cp857', 
            'cp862', 'cp737', 'latin1', 'iso8859-1', 'iso8859-2', 'iso8859-3', 
            'iso8859-4', 'iso8859-5', 'iso8859-6', 'iso8859-7', 'iso8859-8', 
            'iso8859-9', 'iso8859-10', 'iso8859-13', 'iso8859-14', 'iso8859-15', 
            'iso8859-16', 'maclatin1', 'maclatin2', 'macroman', 'cp1250', 'cp1251', 
            'cp1252', 'cp1253', 'cp1254', 'cp1255', 'cp1256', 'cp1257', 'cp1258', 
            'koi8-r', 'koi8-u', 'macroman', 'maciceland', 'macturkish', 'macgreek', 
            'macukrainian', 'machebrew', 'maccroatian', 'maccyrillic', 'cp037', 'cp273', 
            'cp424', 'cp500', 'cp720', 'cp737', 'cp775', 'cp838', 'cp852', 'cp855', 
            'cp858', 'cp864', 'cp869', 'cp870', 'cp875', 'cp880', 'cp905', 'cp1026', 
            'cp1140', 'cp1153', 'cp1160', 'macgreek', 'maclatin2', 'macturkish', 'macukraine',
            'shift_jisx0213', 'windows-874', 'windows-949', 'windows-936', 'windows-950',
            'cp1258', 'utf-16-le', 'utf-16-be', 'utf-32-le', 'utf-32-be', 'cp862', 
            'latin1', 'iso8859-1', 'iso8859-2', 'iso8859-3', 'iso8859-4', 'iso8859-5', 
            'iso8859-6', 'iso8859-7', 'iso8859-8', 'iso8859-9', 'iso8859-10', 
            'iso8859-13', 'iso8859-14', 'iso8859-15', 'iso8859-16', 'maclatin1', 
            'maclatin2', 'macroman', 'cp1250', 'cp1251', 'cp1252', 'cp1253', 'cp1254', 
            'cp1255', 'cp1256', 'cp1257', 'cp1258', 'koi8-r', 'koi8-u', 'macroman', 
            'maciceland', 'macturkish', 'macgreek', 'macukrainian', 'machebrew', 
            'maccroatian', 'maccyrillic', 'cp037', 'cp273', 'cp424', 'cp500', 'cp720', 
            'cp737', 'cp775', 'cp838', 'cp852', 'cp855', 'cp858', 'cp864', 'cp869', 
            'cp870', 'cp875', 'cp880', 'cp905', 'cp1026', 'cp1140', 'cp1153', 'cp1160',
            'cp28591', 'cp28592', 'cp28593', 'cp28594', 'cp28595', 'cp28596', 
            'cp28597', 'cp28598', 'cp28599', 'cp28600', 'cp28601', 'cp28602', 
            'cp28603', 'cp28604', 'cp28605', 'cp28606', 'cp28607', 'cp28608', 
            'cp28609', 'cp28610', 'cp28611', 'cp28612', 'cp28613', 'cp28614', 
            'cp28615', 'cp28616', 'cp28617', 'cp28618', 'cp28619', 'cp28620', 
            'cp28621', 'cp28622', 'cp28623', 'cp28624', 'cp28625', 'cp28626', 
            'cp28627', 'cp28628', 'cp28629', 'cp28630', 'cp28631', 'cp28632', 
            'cp28633', 'cp28634', 'cp28635', 'cp28636', 'cp28637', 'cp28638', 
            'cp28639', 'cp28640', 'cp28641', 'cp28642', 'cp28643', 'cp28644', 
            'cp28645', 'cp28646', 'cp28647', 'cp28648', 'cp28649', 'cp28650', 
            'cp28651', 'cp28652', 'cp28653', 'cp28654', 'cp28655', 'cp28656', 
            'cp28657', 'cp28658', 'cp28659', 'cp28660', 'cp28661', 'cp28662', 
            'cp28663', 'cp28664', 'cp28665', 'cp28666', 'cp28667', 'cp28668', 
            'cp28669', 'cp28670', 'cp28671', 'cp28672', 'cp28673', 'cp28674', 
            'cp28675', 'cp28676', 'cp28677', 'cp28678', 'cp28679', 'cp28680', 
            'cp28681', 'cp28682', 'cp28683', 'cp28684', 'cp28685', 'cp28686', 
            'cp28687', 'cp28688', 'cp28689', 'cp28690', 'cp28691', 'cp28692', 
            'cp28693', 'cp28694', 'cp28695', 'cp28696', 'cp28697', 'cp28698', 
            'cp28699', 'cp28700', 'cp28701', 'cp28702', 'cp28703', 'cp28704', 
            'cp28705', 'cp28706', 'cp28707', 'cp28708', 'cp28709', 'cp28710', 
            'cp28711', 'cp28712', 'cp28713', 'cp28714', 'cp28715', 'cp28716', 
            'cp28717', 'cp28718', 'cp28719', 'cp28720', 'cp28721', 'cp28722', 
            'cp28723', 'cp28724', 'cp28725', 'cp28726', 'cp28727', 'cp28728', 
            'cp28729', 'cp28730', 'cp28731', 'cp28732', 'cp28733', 'cp28734', 
            'cp28735', 'cp28736', 'cp28737', 'cp28738', 'cp28739', 'cp28740', 
            'cp28741', 'cp28742', 'cp28743', 'cp28744', 'cp28745', 'cp28746', 
            'cp28747', 'cp28748', 'cp28749', 'cp28750', 'cp28751', 'cp28752', 
            'cp28753', 'cp28754', 'cp28755', 'cp28756', 'cp28757', 'cp28758', 
            'cp28759', 'cp28760', 'cp28761', 'cp28762', 'cp28763', 'cp28764', 
            'cp28765', 'cp28766', 'cp28767', 'cp28768', 'cp28769', 'cp28770', 
            'cp28771', 'cp28772', 'cp28773', 'cp28774', 'cp28775', 'cp28776', 
            'cp28777', 'cp28778', 'cp28779', 'cp28780', 'cp28781', 'cp28782', 
            'cp28783', 'cp28784', 'cp28785', 'cp28786', 'cp28787', 'cp28788', 
            'cp28789', 'cp28790', 'cp28791', 'cp28792', 'cp28793', 'cp28794', 
            'cp28795', 'cp28796', 'cp28797', 'cp28798', 'cp28799', 'cp28800'
    ]

    for encoding in encodings:
        try:
            with open(input_file, 'r', encoding=encoding) as f:
                lines = f.readlines()
            break  # Si la lectura es exitosa, sal del bucle
        except Exception as e:
            print(f"Error leyendo el archivo con la codificación {encoding}: {e}")
    else:
        print("No se pudo leer el archivo con ninguna de las codificaciones proporcionadas.")
        return [], 0, 0

    filtered_lines = []
    line_counts = collections.Counter()
    short_password_count = 0

    for line in lines:
        parts = line.strip().split(':')
        if len(parts) != 2:
            continue  # Ignora las líneas que no tienen exactamente un par email:password
        email, password = parts
        if len(password) > 4:
            filtered_lines.append(f"{email}:{password}")
            line_counts[f"{email}:{password}"] += 1
        else:
            short_password_count += 1

    unique_lines = []
    duplicate_count = 0

    for line, count in line_counts.items():
        if count == 1:
            unique_lines.append(line)
        else:
            duplicate_count += count

    return unique_lines, duplicate_count, short_password_count

def save_to_file(content, output_file):
    with open(output_file, 'w') as f:
        for line in content:
            f.write(f"{line}\n")

def open_file_dialog():
    file_path = filedialog.askopenfilename(filetypes=[("Text files", "*.txt")])
    return file_path

def save_file_dialog(content):
    file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text files", "*.txt")])
    if file_path:
        save_to_file(content, file_path)

def main():
    root = tk.Tk()
    root.title("Organizador - BSZ/Emails:Passwords")
    root.geometry("600x600")

    # Obtener las dimensiones de la pantalla
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()

    # Calcular la posición para centrar la ventana
    window_width = 600
    window_height = 600
    position_top = int(screen_height / 2 - window_height / 2)
    position_right = int(screen_width / 2 - window_width / 2)

    root.geometry(f"{window_width}x{window_height}+{position_right}+{position_top}")

    def process_and_display():
        input_file = open_file_dialog()
        if not input_file:
            print("No se seleccionó ningún archivo.")
            return

        start_time = time.time()  # Inicio del contador de tiempo
        unique_lines, duplicate_count, short_password_count = process_file(input_file)
        end_time = time.time()  # Fin del contador de tiempo

        elapsed_time = end_time - start_time
        results_text.delete(1.0, tk.END)
        results_text.insert(tk.END, "\n".join(unique_lines))

        stats_text.set(f"Total de entradas duplicadas: {duplicate_count}\n"
                       f"Total de entradas únicas: {len(unique_lines)}\n"
                       f"Total de entradas con contraseñas de 4 o menos caracteres: {short_password_count}\n"
                       f"Tiempo total de procesamiento: {elapsed_time:.2f} segundos")

    def save_results():
        save_file_dialog(results_text.get(1.0, tk.END).splitlines())

    # Crear frame para las estadísticas
    stats_frame = tk.Frame(root)
    stats_frame.pack(side=tk.TOP, fill=tk.X, padx=10, pady=5)

    stats_text = tk.StringVar()
    stats_label = tk.Label(stats_frame, textvariable=stats_text, justify=tk.LEFT, anchor="w")
    stats_label.pack(side=tk.LEFT)

    process_button = tk.Button(root, text="Seleccionar y Procesar Archivo", command=process_and_display)
    process_button.pack(pady=10)

    save_button = tk.Button(root, text="Guardar Resultados", command=save_results)
    save_button.pack(pady=10)

    results_text = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=70, height=20)
    results_text.pack(pady=10)

    # Título en la esquina inferior derecha
    title_label = tk.Label(root, text="Organizador BSZ", font=("Arial", 24), anchor="e")
    title_label.pack(side=tk.BOTTOM, anchor="e", padx=10, pady=(0, 30))  # Posiciona el título justo encima del crédito

    # Crédito en la parte inferior
    credit_label = tk.Label(root, text="echo por AvaStrOficial", font=("Arial", 10))
    credit_label.pack(side=tk.BOTTOM, pady=(0, 10))

    root.mainloop()

if __name__ == "__main__":
    main()
