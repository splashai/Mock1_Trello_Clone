import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex);
import axios from "axios";

export default new Vuex.Store({
    // strict : true, // Todo Reinstate back.
    
    state : {
        selectedComponent : 'Selected Component',
        boards : [],
    },

    getters : {
        selectedComponent : state => {
            return state.selectedComponent;
        },

        getBoards : state => {
            return state.boards;
        },
    },

    mutations : {
        getBoardsAPI : state => {
            axios.get(`http://127.0.0.1:8000/api/v1/boards/`)
            .then(response => {
                state.boards = response.data;
            });
        //     .catch(e => {
        //         this.errors.push(e);
        // });
        },
    },
});