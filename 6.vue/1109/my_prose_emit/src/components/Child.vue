<template>
  <div>
    <h1>This is Child</h1>
    <p>ChildData: {{childData}}</p>
    <input v-model="childData" type="text" @input="inputChildData">
    <p>appData: {{ appData }}</p>
    <p>parentData: {{ parentData }}</p>

  </div>
</template>

<script>
export default {
  name:'Child',
  data: function () {
    return {
      childData: ''
    }
  },
  // 아래서 위로 보낼때 *methods s중요!
  methods: {
    inputChildData: function () {
      this.$emit('child-input', this.childData)
    }
  },
  props: {
    appData: String,
    parentData: String,
  }
}
</script>