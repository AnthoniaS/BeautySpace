<template>
  <nav class="navbar navbar-expand-sm bg-primary navbar-dark mb-3">
    <img src="beauty.png" alt="bs" class="mx-3" />
    <router-link class="navbar-brand" to="/">BS</router-link>
    <router-link class="navbar-brand text-right" to="/agendamentos">Agendamento</router-link>
    <router-link class="navbar-brand text-right" to="/agendados">Clientes Agendados</router-link>

    <ul class="navbar-nav ml-auto">
      <li class="nav-item dropdown">
        <a class="nav-link dropdown-toggle" href="#" id="navbardrop" data-toggle="dropdown">
          <i class="fas fa-user mr-1"></i>
          <span v-if="user">{{user}}</span>
          <span v-else>(Não Logado)</span>
        </a>
        <div class="dropdown-menu">
          <router-link class="dropdown-item" to="/login">Login</router-link>
          <a class="dropdown-item" href="#" @click="sair">Logout</a>
        </div>
      </li>
    </ul>
  </nav>
</template>

<script>
export default {
  props: {
    user: String
  },
  methods: {
    sair() {
      localStorage.removeItem("token");
      this.$parent.mudaUser(null);
    }
  }
};
</script>

<style scoped>
img {
  width: 250px;
  height: 100px;
}
</style>