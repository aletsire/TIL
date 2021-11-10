<template>
<div>
  <input @keypress.enter="onInputKeyword" type="text">

</div>
  
</template>

<script>
export default {
  name:'SearchBar',
  methods: {
    onInputKeyword: function (event) {
      //console.log(event.target.value)
      // 두개 이상을 보낼때는 이렇게?
      //this.$emit('input-search', event.target.value, 'additional payload')
      this.$emit('input-search', event.target.value)
    },

  }
}
</script>

<style>

</style>