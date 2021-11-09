<template>
  <div id="app">
    <!-- 3. 사용하기 -->
    <h1>App</h1>
    <p>Appdata: {{ appData }}</p>
    <input v-model="appData" type="text">
    <p>ParentData: {{parentData}}</p>
    <p>ChildData: {{childData}}</p>
    <!-- :보내는 이름="보낼내용" -->
    <Parent :appData="appData" 
    @parent-input="inputParentData" @child-input="inputChildData"/>

  </div>
</template>

<script>
// 1. 불러오기
import Parent from './components/Parent.vue'


export default {
  name: 'App',
  // 2. 등록하기
  components: {
    Parent,
  },
  data: function () {
    return  {
      appData: '',
      parentData: '',
      childData: ''
    }
  },
  methods: {
    inputParentData: function(data) {
      this.parentData = data
    },
    inputChildData: function(data) {
      this.childData = data
    }
  },
  // data는 function으로
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
