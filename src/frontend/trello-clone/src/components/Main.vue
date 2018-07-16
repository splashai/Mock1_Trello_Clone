<template>
  <div class="container">
    
    <app-boards></app-boards>
    <app-board v-if="getBoardDetails"></app-board>

  </div>
</template>

<script>

import Boards from './Boards';
import Board from './Board';
import { mapGetters } from 'vuex';

export default {
  

    components :{
      'app-boards' : Boards,
      'app-board' : Board,
    },

    computed :{
    ...mapGetters([
      'getBoardDetails',
    ]),

    },
  
};

</script>