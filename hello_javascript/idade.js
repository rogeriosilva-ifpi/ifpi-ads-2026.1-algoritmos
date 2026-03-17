import { question } from 'readline-sync'

function main(){
  const nome = question('Qual seu nome? ')
  const ano_nascimento = Number(question('Qual ano de nascimento: '))
  const sexo = question('Qual sexo (M ou F): ').toUpperCase()

  const idade = 2026 - ano_nascimento

  console.log(`Olá ${nome}!`)

  if (idade >= 18){
    console.log(`Em 2026 você terá ${idade} anos.`)
  }

  if (vai_para_guerra(idade, sexo)){
    console.log(`Olá ${nome} você defenderá nosso país!`)
  }else{
    console.log(`Sinto muito. Você não vai nos salvar!`)
  }

}


function vai_para_guerra(idade, sexo){
  return idade >= 18 && sexo === 'M'
}

main()