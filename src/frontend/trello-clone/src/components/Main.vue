<template>
  <div class="container">
    
    <app-boards></app-boards>
    <app-board></app-board>

  </div>
</template>

<script>

import Boards from './Boards'
import Board from './Board'

export default {

    components :{
      'app-boards' : Boards,
      'app-board' : Board,
    },
  
};

</script>