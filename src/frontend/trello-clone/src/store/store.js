import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex);


export const store = new Vuex.Store({
    strict : true,

    state : {
        selectedComponent : 'Selected Component'
    },

    getters : {
        selectedComponent () {
            return state.selectedComponent;
        }
    }

});