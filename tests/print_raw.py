
# recebe vários inputs com \n separado em listas
if __name__ == '__main__':
    print("Texto:")
    lines = []
    while True:
        line = input()
        if not line.strip():  # Para quando a linha estiver vazia
            break
        lines.append(line)

    print(fr"{lines}")
    print()
    txt = "\n".join(lines)
    print(txt.__repr__())