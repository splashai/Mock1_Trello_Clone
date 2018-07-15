<template>
    <div>
        {{getBoardDetails}}
    </div>

</template>

<script>
import { mapGetters, mapMutations, mapActions } from 'vuex'

export default {
  data() {
    return {
      
    };
  },

  methods : {

    
  },


  computed : {

    ...mapGetters([
      'getBoardDetails',
    ]),

    

  }, // End of computed

};

</script>


<style scoped>
    
</style>