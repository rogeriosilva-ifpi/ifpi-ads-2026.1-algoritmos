import turtle

def main():
  bob = turtle.Turtle()

  bob.shape('turtle')
  
  # bob.pencolor('red')
  # desenhar_quadrado(bob, 100)
  
  # bob.pencolor('blue')
  # desenhar_quadrado(bob, 200)

  # poligono(bob, 200, 5)
  # bob.pencolor('blue')
  # desenhar_quadrado(bob, 200)

  # poligono(bob, 150, 3)
  escrever_letra(bob, 'L')


  # turtle.mainloop()


def desenhar_quadrado(tartaruga, lado):
  # for i in range(4):
  #   tartaruga.forward(lado)
  #   tartaruga.right(90)
  poligono(tartaruga, lado, 4)


def poligono(tartaruga, lado, n):
  grau = 360 / n
  
  for i in range(n):
    tartaruga.forward(lado)
    tartaruga.left(grau)

def escrever_letra(t: turtle.Turtle, letra):
  t.right(90)
  if letra == 'l' or letra == 'L':
    t.fd(300)
    t.left(90)
    t.fd(150)




main()