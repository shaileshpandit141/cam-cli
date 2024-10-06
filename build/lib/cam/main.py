from cam.controller import controller


def main():
    message = controller()

    if message is not None:
        print(f':: {message}')


if __name__ == "__main__":
    main()
