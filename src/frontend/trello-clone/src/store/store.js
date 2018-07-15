import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex);
import axios from "axios";

export default new Vuex.Store({
    // strict : true, // Todo Reinstate back.

    state: {
        boards: [],
        selectedBoard: '',
        selectedBoardDetails: '',
    }, // End of state

    getters: {
        selectedComponent: state => {
            return state.selectedComponent;
        },

        getBoards: state => {
            return state.boards;
        },

        getBoardDetails : state => {
            return state.selectedBoardDetails;
        },
        
    }, // End of getters

    mutations: {
        getBoardsAPI: state => {
            axios.get(`http://127.0.0.1:8000/api/v1/boards/`)
                .then(response => {
                    state.boards = response.data;
                });
            //     .catch(e => {
            //         this.errors.push(e);
            // });
        },

        setBoardDetails: (state, payload) => {
            state.selectedBoard = payload.url;
            state.selectedBoardDetails = payload.data;
        },

        
    }, // End of mutations.

    actions: {
        getBoardDetailsAPI: (context, payload) => {
            axios.get(payload.url)
                .then(response => {
                    context.commit('setBoardDetails', {
                        url: payload.url,
                        data: response.data,
                    });
                });
        },
    }, // End of actions

});