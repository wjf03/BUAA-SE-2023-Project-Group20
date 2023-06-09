import axiosInstance from './index'

const axios = axiosInstance

export const getNotes = (user_id, book_id) => {
    return axios.post('http://127.0.0.1:8000/note/view_all_note/'+user_id+'/'+book_id)
}

export const createNote = (user_id, book_id, color, content, range, note, cfi) => {
    return axios.post('http://127.0.0.1:8000/note/create_note',
    {
        'user_id': user_id,
        'book_id': book_id,
        'chapter_id': 0,
        'color': color.toString(),
        'content': content,
        'range1': range,
        'note': note,
        'cfi': cfi

    })
}

export const updateNoteColor = (note_range, color) => {
    return axios.post('http://127.0.0.1:8000/note/update_note_color',
    {'range':note_range, 'color':color})
}

export const updateNoteText = (note_range, text) => {
    return axios.post('http://127.0.0.1:8000/note/update_note_text',
    {'range':note_range, 'text':text})
}

export const deleteNote = (note_range) => {
    return axios.post('http://127.0.0.1:8000/note/delete_note',{'range' : note_range})
}

export const createLabel = (user_id, book_id, cfi, percentage, time) => {
    return axios.post('http://127.0.0.1:8000/label/add_label',
    {
        'user_id': user_id,
        'book_id': book_id,
        'chapter_id': 0,
        'cfi': cfi,
        'percentage': percentage,
        'time':time
    })
}

export const getLabels = (user_id, book_id) => {
    return axios.post('http://127.0.0.1:8000/label/search_label',
    { 'user_id': user_id, 'book_id': book_id })
}

export const deleteLabels = (time) => {
    return axios.post('http://127.0.0.1:8000/label/delete_label',
    { 'time': time })
}

export const getBookSource = (book_id) => {
    return axios.post('http://127.0.0.1:8000/book/getBookSource',
    { 'id': book_id })
}