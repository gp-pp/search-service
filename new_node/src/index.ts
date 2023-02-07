import express from 'express';
import { json } from 'body-parser';
import { todoRouter } from './routes/todo';
import mongoose from 'mongoose';
import cors from 'cors';

const app = express();
app.use(cors())

app.use((req, res, next) => {
  res.header('Access-Control-Allow-Origin', '*')
  res.header(
    'Access-Control-Allow-Headers',
    'Origin, X-Requested-With, Content-Type, Accept'
  )
  next()
})

app.use(json());
app.use(todoRouter);

// const url = 'mongodb+srv://harshxtanwar:db12345@cluster0.dvbpycz.mongodb.net/gp_profiles?retryWrites=true&w=majority';

// mongoose.set('strictQuery', true);

// const schema = new mongoose.Schema({
//   _id: String,
//   thumbnail: String,
//   name: String,
//   link: String,
//   author_id: String,
//   email: String,
//   affiliations: String,
//   cited_by: Number,
//   interests: Array,
//   articles: Array
// });

// const Collection = mongoose.model('proff_datas', schema);


// mongoose.connect(url, () => {
//   console.log('connected to database');
//   const search = async () => {
//     const data = await Collection.find({})
//     console.log(data)
//   }


//   search()
// });

// ------------------------

//   Collection.find({}, (err: any, data: any) => {
//     if (err) return console.error(err);
//     console.log(data);
//   });



app.listen(3003, () => {
  console.log('server is listening on port 3003');
});





