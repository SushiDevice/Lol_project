

export default async function Home() {
  const data = await fetch('http://127.0.0.1:8000/pokemon/pikachu')
  const response = await data.json()
  console.log(response)
  return (
    <div>
      <p> {response.name} </p>
      <img src={response.sprite} alt="Pikachu" width={200} height={200} />
      {response["shiny"] == true ? (
        <p>{response["message"]}</p>
      ) : (
        <p>{response["message"]}</p>
      )
      }
    </div> 
  );
}
