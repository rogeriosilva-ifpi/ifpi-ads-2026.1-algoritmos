import { question } from 'readline-sync'

function main(){
  const clube = question("Clube: ")
  const qtd = Number(question('Quantas vezes foi campeão? '))

  for (let i = 0; i < qtd; i++){
    console.log(`${i} - ${clube}`)
  }
  
  console.log('Fim.')

}


main()