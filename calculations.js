//size of each column for piece of paper

let columns = 12, pageInches = 11;

for (let i = 0; i < columns; i++){
  let size = pageInches/columns;
  let round = i*size;
  let result = Math.round(round * 100) / 100;
  console.log(result);
}



