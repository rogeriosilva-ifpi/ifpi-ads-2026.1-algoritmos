import { question } from 'readline-sync'

function main(){
  const inicial = Number(question('Inicial: '))
  const razao = Number(question('Razão: '))
  const limite = Number(question('Limite: '))

  let resultado = ''
  for(let numero = inicial; numero < limite; numero = numero + razao){
    resultado = resultado + ' ' + numero
  }

  console.log(resultado)

}


main()