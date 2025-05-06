import blessed

term = blessed.Terminal()


class Font:
    """
    Font

    This font is a modified version of this font: https://patorjk.com/software/taag/#p=display&f=Big
    """

    def drawSpace(x: int, y: int) -> int:
        print(term.move_xy(x, y + 0) + f":::::", end='')
        print(term.move_xy(x, y + 1) + f":::::", end='')
        print(term.move_xy(x, y + 2) + f":::::", end='')
        print(term.move_xy(x, y + 3) + f":::::", end='')
        print(term.move_xy(x, y + 4) + f":::::", end='')
        print(term.move_xy(x, y + 5) + f":::::", end='')
        print(term.normal, end='', flush=True)
        return 5

    def draw1(x: int, y: int) -> int:
        print(term.move_xy(x, y + 0) + f"::'{term.yellow}##{term.white}:::", end='')
        print(term.move_xy(x, y + 1) + f"'{term.yellow}####{term.white}:::", end='')
        print(term.move_xy(x, y + 2) + f":: {term.yellow}##{term.white}:::", end='')
        print(term.move_xy(x, y + 3) + f":: {term.yellow}##{term.white}:::", end='')
        print(term.move_xy(x, y + 4) + f"'{term.yellow}######{term.white}:", end='')
        print(term.move_xy(x, y + 5) + f"......::", end='')
        print(term.normal, end='', flush=True)
        return 8

    def draw2(x: int, y: int) -> int:
        print(term.move_xy(x, y + 0) + f":'{term.yellow}#####{term.white}::", end='')
        print(term.move_xy(x, y + 1) + f"..... {term.yellow}##{term.white}:", end='')
        print(term.move_xy(x, y + 2) + f":'{term.yellow}#####{term.white}::", end='')
        print(term.move_xy(x, y + 3) + f"'{term.yellow}##{term.white}::::::", end='')
        print(term.move_xy(x, y + 4) + f" {term.yellow}#######{term.white}:", end='')
        print(term.move_xy(x, y + 5) + f".......::", end='')
        print(term.normal, end='', flush=True)
        return 9

    def draw3(x: int, y: int) -> int:
        print(term.move_xy(x, y + 0) + f":'{term.yellow}#####{term.white}::", end='')
        print(term.move_xy(x, y + 1) + f"'.... {term.yellow}##{term.white}:", end='')
        print(term.move_xy(x, y + 2) + f":'{term.yellow}#####{term.white}::", end='')
        print(term.move_xy(x, y + 3) + f":.... {term.yellow}##{term.white}:", end='')
        print(term.move_xy(x, y + 4) + f". {term.yellow}#####{term.white}::", end='')
        print(term.move_xy(x, y + 5) + f":.....:::", end='')
        print(term.normal, end='', flush=True)
        return 9

    def drawA(x: int, y: int) -> int:
        print(term.move_xy(x, y + 0) + f":::'{term.yellow}##{term.white}::::", end='')
        print(term.move_xy(x, y + 1) + f":'{term.yellow}##{term.white}. {term.yellow}##{term.white}::", end='')
        print(term.move_xy(x, y + 2) + f"'{term.yellow}##{term.white}::. {term.yellow}##{term.white}:", end='')
        print(term.move_xy(x, y + 3) + f" {term.yellow}########{term.white}:", end='')
        print(term.move_xy(x, y + 4) + f" {term.yellow}##{term.white}::: {term.yellow}##{term.white}:", end='')
        print(term.move_xy(x, y + 5) + f"..::::..::", end='')
        print(term.normal, end='', flush=True)
        return 9

    def drawD(x: int, y: int) -> int:
        print(term.move_xy(x, y + 0) + f"'{term.yellow}######{term.white}::", end='')
        print(term.move_xy(x, y + 1) + f" {term.yellow}##{term.white}.. {term.yellow}##{term.white}:", end='')
        print(term.move_xy(x, y + 2) + f" {term.yellow}##{term.white}:: {term.yellow}##{term.white}:", end='')
        print(term.move_xy(x, y + 3) + f" {term.yellow}##{term.white}:: {term.yellow}##{term.white}:", end='')
        print(term.move_xy(x, y + 4) + f" {term.yellow}######{term.white}::", end='')
        print(term.move_xy(x, y + 5) + f"......:::", end='')
        print(term.normal, end='', flush=True)
        return 9

    def drawE(x: int, y: int) -> int:
        print(term.move_xy(x, y + 0) + f"'{term.yellow}######{term.white}:", end='')
        print(term.move_xy(x, y + 1) + f" {term.yellow}##{term.white}....:", end='')
        print(term.move_xy(x, y + 2) + f" {term.yellow}#####{term.white}::", end='')
        print(term.move_xy(x, y + 3) + f" {term.yellow}##{term.white}...::", end='')
        print(term.move_xy(x, y + 4) + f" {term.yellow}######{term.white}:", end='')
        print(term.move_xy(x, y + 5) + f".......:", end='')
        print(term.normal, end='', flush=True)
        return 8

    def drawF(x: int, y: int) -> int:
        print(term.move_xy(x, y + 0) + f"'{term.yellow}######{term.white}:", end='')
        print(term.move_xy(x, y + 1) + f" {term.yellow}##{term.white}...::", end='')
        print(term.move_xy(x, y + 2) + f" {term.yellow}#####{term.white}::", end='')
        print(term.move_xy(x, y + 3) + f" {term.yellow}##{term.white}:::::", end='')
        print(term.move_xy(x, y + 4) + f" {term.yellow}##{term.white}:::::", end='')
        print(term.move_xy(x, y + 5) + f"..::::::", end='')
        print(term.normal, end='', flush=True)
        return 8

    def drawI(x: int, y: int) -> int:
        print(term.move_xy(x, y + 0) + f"'{term.yellow}####{term.white}:", end='')
        print(term.move_xy(x, y + 1) + f": {term.yellow}##{term.white}::", end='')
        print(term.move_xy(x, y + 2) + f": {term.yellow}##{term.white}::", end='')
        print(term.move_xy(x, y + 3) + f": {term.yellow}##{term.white}::", end='')
        print(term.move_xy(x, y + 4) + f"'{term.yellow}####{term.white}:", end='')
        print(term.move_xy(x, y + 5) + f"....::", end='')
        print(term.normal, end='', flush=True)
        return 6

    def drawL(x: int, y: int) -> int:
        print(term.move_xy(x, y + 0) + f"'{term.yellow}##{term.white}:::::", end='')
        print(term.move_xy(x, y + 1) + f" {term.yellow}##{term.white}:::::", end='')
        print(term.move_xy(x, y + 2) + f" {term.yellow}##{term.white}:::::", end='')
        print(term.move_xy(x, y + 3) + f" {term.yellow}##{term.white}:::::", end='')
        print(term.move_xy(x, y + 4) + f" {term.yellow}######{term.white}:", end='')
        print(term.move_xy(x, y + 5) + f"......::", end='')
        print(term.normal, end='', flush=True)
        return 8

    def drawM(x: int, y: int) -> int:
        print(term.move_xy(x, y + 0) + f"'{term.yellow}##{term.white}::::'{term.yellow}##{term.white}:", end='')
        print(term.move_xy(x, y + 1) + f" {term.yellow}####{term.white}'{term.yellow}####{term.white}:", end='')
        print(term.move_xy(x, y + 2) + f" {term.yellow}## ### ##{term.white}:", end='')
        print(term.move_xy(x, y + 3) + f" {term.yellow}##{term.white}. {term.yellow}#{term.white}: {term.yellow}##{term.white}:", end='')
        print(term.move_xy(x, y + 4) + f" {term.yellow}##{term.white}:::: {term.yellow}##{term.white}:", end='')
        print(term.move_xy(x, y + 5) + f"..:::::..::", end='')
        print(term.normal, end='', flush=True)
        return 11

    def drawN(x: int, y: int) -> int:
        print(term.move_xy(x, y + 0) + f"'{term.yellow}##{term.white}::: {term.yellow}##{term.white}:", end='')
        print(term.move_xy(x, y + 1) + f" {term.yellow}####{term.white}: {term.yellow}##{term.white}:", end='')
        print(term.move_xy(x, y + 2) + f" {term.yellow}## ## ##{term.white}:", end='')
        print(term.move_xy(x, y + 3) + f" {term.yellow}##{term.white}. {term.yellow}####{term.white}:", end='')
        print(term.move_xy(x, y + 4) + f" {term.yellow}##{term.white}::. {term.yellow}##{term.white}:", end='')
        print(term.move_xy(x, y + 5) + f"..::::..::", end='')
        print(term.normal, end='', flush=True)
        return 10

    def drawO(x: int, y: int) -> int:
        print(term.move_xy(x, y + 0) + f":'{term.yellow}#####{term.white}::", end='')
        print(term.move_xy(x, y + 1) + f"'{term.yellow}##{term.white}.. {term.yellow}##{term.white}:", end='')
        print(term.move_xy(x, y + 2) + f" {term.yellow}##{term.white}:: {term.yellow}##{term.white}:", end='')
        print(term.move_xy(x, y + 3) + f" {term.yellow}##{term.white}:: {term.yellow}##{term.white}:", end='')
        print(term.move_xy(x, y + 4) + f". {term.yellow}#####{term.white}::", end='')
        print(term.move_xy(x, y + 5) + f":.....:::", end='')
        print(term.normal, end='', flush=True)
        return 9

    def drawR(x: int, y: int) -> int:
        print(term.move_xy(x, y + 0) + f"'{term.yellow}#######{term.white}::", end='')
        print(term.move_xy(x, y + 1) + f" {term.yellow}##{term.white}... {term.yellow}##{term.white}:", end='')
        print(term.move_xy(x, y + 2) + f" {term.yellow}#######{term.white}::", end='')
        print(term.move_xy(x, y + 3) + f" {term.yellow}##{term.white}. {term.yellow}##{term.white}:::", end='')
        print(term.move_xy(x, y + 4) + f" {term.yellow}##{term.white}::. {term.yellow}##{term.white}:", end='')
        print(term.move_xy(x, y + 5) + f"..::::..::", end='')
        print(term.normal, end='', flush=True)
        return 10

    def drawS(x: int, y: int) -> int:
        print(term.move_xy(38, y + 0) + f":'{term.yellow}#####{term.white}::", end='')
        print(term.move_xy(38, y + 1) + f" {term.yellow}##{term.white}....::", end='')
        print(term.move_xy(38, y + 2) + f". {term.yellow}#####{term.white}::", end='')
        print(term.move_xy(38, y + 3) + f":.... {term.yellow}##{term.white}:", end='')
        print(term.move_xy(38, y + 4) + f". {term.yellow}#####{term.white}::", end='')
        print(term.move_xy(38, y + 5) + f":.....:::", end='')
        print(term.normal, end='', flush=True)
        return 9

    def drawT(x: int, y: int) -> int:
        print(term.move_xy(x, y + 0) + f"'{term.yellow}######{term.white}:", end='')
        print(term.move_xy(x, y + 1) + f".. {term.yellow}##{term.white}.::", end='')
        print(term.move_xy(x, y + 2) + f":: {term.yellow}##{term.white}:::", end='')
        print(term.move_xy(x, y + 3) + f":: {term.yellow}##{term.white}:::", end='')
        print(term.move_xy(x, y + 4) + f":: {term.yellow}##{term.white}:::", end='')
        print(term.move_xy(x, y + 5) + f"::..::::", end='')
        print(term.normal, end='', flush=True)
        return 8

    def drawU(x: int, y: int) -> int:
        print(term.move_xy(x, y + 0) + f"'{term.yellow}##{term.white}::'{term.yellow}##{term.white}:", end='')
        print(term.move_xy(x, y + 1) + f" {term.yellow}##{term.white}:: {term.yellow}##{term.white}:", end='')
        print(term.move_xy(x, y + 2) + f" {term.yellow}##{term.white}:: {term.yellow}##{term.white}:", end='')
        print(term.move_xy(x, y + 3) + f" {term.yellow}##{term.white}:: {term.yellow}##{term.white}:", end='')
        print(term.move_xy(x, y + 4) + f". {term.yellow}#####{term.white}::", end='')
        print(term.move_xy(x, y + 5) + f":.....:::", end='')
        print(term.normal, end='', flush=True)
        return 9

    def drawY(x: int, y: int) -> int:
        print(term.move_xy(52, y + 0) + f"'{term.yellow}##{term.white}:::'{term.yellow}##{term.white}:", end='')
        print(term.move_xy(52, y + 1) + f". {term.yellow}##{term.white}:'{term.yellow}##{term.white}::", end='')
        print(term.move_xy(52, y + 2) + f":. {term.yellow}####{term.white}:::", end='')
        print(term.move_xy(52, y + 3) + f"::. {term.yellow}##{term.white}::::", end='')
        print(term.move_xy(52, y + 4) + f"::: {term.yellow}##{term.white}::::", end='')
        print(term.move_xy(52, y + 5) + f":::..:::::", end='')
        print(term.normal, end='', flush=True)
        return 10

    def print(x: int, y: int, text: str) -> int:
        for character in text:
            if character == ' ':
                x += Font.drawSpace(x, y)
            else:
                x += Font.__dict__['draw' + str(character)](x, y)
        return x
