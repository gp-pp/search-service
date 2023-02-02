import mongoose from 'mongoose';

// interface ITodo {
//     title: string;
//     description: string;
// }

// function test(name: ITodo) {}

const todoSchema = new mongoose.Schema({
    title: {
        type: String,
        required: true
    },
    description: {
        type: String,
        required: true
    }
})

const Todo = mongoose.model('Todo', todoSchema)


new Todo({
    titl: 'kuch to hai',
    description: 'kuch to hai bhai'
})

new Todo({
    title: 'kuch to hai',
    description: 'kuch to hai bhai',
    hour: 1
})


export {Todo}

// ml