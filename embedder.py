def embed_script(image_file, script_file, output_file):
    with open(image_file, 'rb') as img_file:
        img_data = img_file.read()
    
    with open(script_file, 'rb') as s_file:
        script_data = s_file.read()
    
    with open(output_file, 'wb') as out_file:
        out_file.write(img_data)
        out_file.write(b'\x00\x00\x00\x00')  # Adding a delimiter
        out_file.write(script_data)

# Example usage
embed_script('promo-code.png', 'innocentfile.py', 'promo.png')