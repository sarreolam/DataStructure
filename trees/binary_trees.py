import pygame

class Node:
    def __init__(self, value) -> None:
        self.value = value
        self.parent: None | "Node" = None
        self.left: None | "Node" = None
        self.right: None | "Node" = None

    def __repr__(self) -> str:
        parent = "None"
        left = "None"
        right = "None"

        if self.parent:
            parent = self.parent.value

        if self.left:
            left = self.left.value

        if self.right:
            right = self.right.value

        return f'Node: {{\n  value: {self.value},\n  parent: {parent},\n  left: {left},\n  right: {right}\n}}'

class BST:
    def __init__(self) -> None:
        self.root = None

    def insert(self, value):
        node = Node(value)

        if not self.root:
            self.root = node
            return node

        curr_node = self.root

        while True:
            if value < curr_node.value:
                if not curr_node.left:
                    curr_node.left = node
                    node.parent = curr_node
                    return node
                else:
                    node.parent = curr_node
                    curr_node = curr_node.left
            elif value > curr_node.value:
                if not curr_node.right:
                    curr_node.right = node
                    node.parent = curr_node
                    return node
                else:
                    node.parent = curr_node
                    curr_node = curr_node.right

    def inorder(self, node: Node | None) -> list[int]:
        if not node:
            return []

        return self.inorder(node.left) + [node.value] + self.inorder(node.right)

    def search(self, value: int) -> Node | None:
        curr_node = self.root

        while True:
            if not curr_node:
                return None

            if curr_node.value == value:
                return curr_node
            elif value < curr_node.value:
                curr_node = curr_node.left
            else:
                curr_node = curr_node.right

    def previous(self, node: Node):
        curr_node = node

        if not curr_node.left:
            while True:
                if not curr_node.parent:
                    return None

                if curr_node.value > curr_node.parent.value:
                    return curr_node.parent

                curr_node = curr_node.parent
        else:
            curr_node = curr_node.left
            while curr_node.right:
                curr_node = curr_node.right

            return curr_node

    def next(self, node: Node):
        curr_node = node

        if not curr_node.right:
            while True:
                if not curr_node.parent:
                    return None

                if curr_node.value < curr_node.parent.value:
                    return curr_node.parent

                curr_node = curr_node.parent
        else:
            curr_node = curr_node.right
            while curr_node.left:
                curr_node = curr_node.left

            return curr_node

    def min(self, node: Node):
        curr_node = node

        while curr_node.left:
            curr_node = curr_node.left

        return curr_node

    def max(self, node: Node):
        curr_node = node

        while curr_node.right:
            curr_node = curr_node.right

        return curr_node

    def height(self, node: Node | None):
        if node is None:
            return 0

        else:
            lDepth = self.height(node.left)
            rDepth = self.height(node.right)

            if (lDepth > rDepth):
                return lDepth+1
            else:
                return rDepth+1

    def depth(self, node: Node | None):
        profundiad = 0
        current = node
        while current:
            current = current.parent
            profundiad += 1
        return profundiad
    
    def delete(self, node: Node):
        if node == self.root:
            if not node.left and node.right:
                self.root = node.right
                node.right.parent=None
                return
            elif not node.right and node.left:
                self.root = node.left
                node.left.parent=None
                return
            elif not node.right and not node.left: return
            else: pass


        if node.right and node.left:
            prev=self.previous(node)
            node.value=prev.value
            node=prev
        if node.right and not node.left:
            if node.value > node.parent.value: node.parent.right=node.right
            else: node.parent.left=node.right
            node.right.parent=node.parent
        elif node.left and not node.right: 
            if node.value > node.parent.value: node.parent.right=node.left
            else: node.parent.left=node.left
            node.left.parent=node.parent
        else:
            if node.value > node.parent.value: node.parent.right=None
            else: node.parent.left=None


    def change(self, node:Node):
        
        if node != self.root:
            if node.value > node.parent.value:
                parent=node.parent
                if node.left:
                    node.parent.right=node.left   
                    node.left.parent=node.parent
                else:
                    node.parent.right=None
                if node.parent.parent:
                    if node.parent.value > node.parent.parent.value:
                        node.parent=parent.parent
                        parent.parent.right=node
                    else:
                        node.parent=parent.parent
                        parent.parent.left=node
                else: 
                    node.parent=None
                    self.root=node
                node.left=parent
                parent.parent=node
                
    
            else: 
                parent=node.parent
                if node.right:
                    node.parent.left=node.right
                    node.right.parent=node.parent
                else:
                    node.parent.left=None
                if node.parent.parent:
                    if node.parent.value > node.parent.parent.value:
                        node.parent=node.parent.parent
                        parent.parent.right=node
                    else:
                        node.parent=node.parent.parent
                        parent.parent.left=node
                else: 
                    node.parent=None
                    self.root=node
                node.right=parent
                parent.parent=node
        # else: print('es raiz')



        

tree = BST()
values = [17, 10, 34, 2, 13, 20, 4, 3, 8, 14, 16, 18, 33, 50, 42, 100, 40, 80, 0, 1, 12]
# values= [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26]

for value in values:
    tree.insert(value)

# tree.change(tree.search(13))
# print("bueans",tree.search(13))

inorder = tree.inorder(tree.root)

pygame.init()

white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
yellow = (255,255,0)

display_size = 500
gameDisplay = pygame.display.set_mode((display_size, display_size))
gameDisplay.fill(black)
font = pygame.font.SysFont("Verdana", 12)
margen = 30
radio = (display_size - 3*margen) / len(values)
clock = pygame.time.Clock()

max_depth = tree.height(tree.root)
class Circle:
    def __init__(self, circle, i) -> None:
        self.figure: pygame.Rect = circle
        self.pos: int = i
        self.color: tuple[int, int, int] = white
        self.value = inorder[i]


def findNodeCoords(node: Node, idx: int):
    x = (display_size - 2 * margen) / len(inorder) * idx + 2 * radio
    y = (display_size - 2 * margen) / max_depth * (tree.depth(node) - 1) + 2 * radio

    return (x, y)

def createTree() -> list[Circle]:
    circulos = []

    for (i, num) in enumerate(inorder):
        curr = tree.search(num)

        if not curr:
            continue

        (x, y) = findNodeCoords(curr, i)
        nuevo_circulo = Circle(pygame.draw.circle(
            gameDisplay, white, (x, y), radio), i)
        circulos.append(nuevo_circulo)

    return circulos

circles = createTree()

def drawButtons():
    of= 15
    buttons=['Eliminar', 'Cambiar', 'Prev y Next']
    rect= []
    for i in range(3):
        rect.append([pygame.draw.rect(gameDisplay, red, (10,(i+1)*of+i*20, 100, 20)), buttons[i]])
        text = font.render(f"{buttons[i]}", True, white, None)
        textRect = text.get_rect()
        textRect.topleft = (20,(i+1)*of+i*20)
        gameDisplay.blit(text, textRect)
    return rect


def drawTree(circles: list[Circle]):
    for (i, num) in enumerate(inorder):
        curr = tree.search(num)

        # Node not found!
        if not curr:
            continue

        (x, y) = findNodeCoords(curr, i)

        if curr.left:
            idLeft = inorder.index(curr.left.value)

            (lX, lY) = findNodeCoords(curr.left, idLeft)
            pygame.draw.line(gameDisplay, white, (x, y), (lX, lY))
        if curr.right:
            idRight = inorder.index(curr.right.value)

            (rX, rY) = findNodeCoords(curr.right, idRight)
            pygame.draw.line(gameDisplay, white, (x, y), (rX, rY))

        
    for (i, num) in enumerate(inorder):
        curr = tree.search(num)

        # Node not found!
        if not curr:
            continue

        (x, y) = findNodeCoords(curr, i)
        pygame.draw.circle(gameDisplay, circles[i].color, (x, y), radio)

        text = font.render(f"{num}", True, black, None)
        textRect = text.get_rect()
        textRect.center = (int(x), int(y))
        gameDisplay.blit(text, textRect)
        pygame.display.update()

drawTree(circles)
rect=drawButtons()
action=rect[2][1]
# print(x)
pygame.display.update()

while True:
    clock.tick(600)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_position = pygame.mouse.get_pos()
            for circle in circles:
                # resetear circulos
                circle.color = white
            
            for button in rect:
                if (button[0].collidepoint( mouse_position ) ): 
                    action = button[1]
                    # print(action)

            for circle in circles:
                if (circle.figure.collidepoint(mouse_position)):
                    node = tree.search(circle.value)
                    circle.color = red

                    # print(node)
                    if action=='Eliminar': 
                        tree.delete(node)
                        max_depth = tree.height(tree.root)
                        inorder = tree.inorder(tree.root)
                        circles = createTree()
                        # drawTree(circles)
                        drawButtons()
                    if action=='Cambiar': 
                        
                        tree.change(node)
                        max_depth = tree.height(tree.root)
                        # print(inorder)
                        inorder = tree.inorder(tree.root)
                        circles = createTree()
                        # drawTree(circles)
                        drawButtons()

                    if action=='Prev y Next':   
                        if node:
                            next = tree.next(node)
                            prev = tree.previous(node)

                            if next:
                                circles[inorder.index(next.value)].color = blue
                            if prev:
                                circles[inorder.index(prev.value)].color = green

                    # print("Presionado:", inorder[circle.pos])
            pygame.draw.rect(gameDisplay, black, (0,0,display_size, display_size))
            
            drawTree(circles)
            drawButtons()
            pygame.display.update()
