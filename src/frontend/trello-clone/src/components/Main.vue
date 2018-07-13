<template>
  <div class="container">
    
    <app-boards></app-boards>

  </div>
</template>

<script>

import Boards from './Boards'

export default {

    components :{
      'app-boards' : Boards,
    },
  
};

</script>