import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex);
import axios from "axios";

export default new Vuex.Store({
    // strict : true, // Todo Reinstate back.
    
    state : {
        selectedComponent : 'Selected Component',
        boards : [
            {name : '1', 'description' :'desc' , create_date : 'sfasdfasfasfasf'
            },
        ],
    },

    getters : {
        selectedComponent : state => {
            return state.selectedComponent;
        },

        getBoards : state => {
            axios.get(`http://127.0.0.1:8000/api/v1/boards/`)
            .then(response => {
                state.boards = response.data;
            });
            //     .catch(e => {
            //         this.errors.push(e);
            // });
            return state.boards;
        },
    },

    mutations : {
        getBoardsAPI() {
            axios.get(`http://127.0.0.1:8000/api/v1/boards/`)
            .then(response => {
                state.boards = response.data;
            });
        //     .catch(e => {
        //         this.errors.push(e);
        // });
        return state.boards;
        },
    },
});