<template>
  <div class="container">
    <h2>
      Agenda
    </h2>
    <table class="table table-striped">
      <thead>
        <tr>
          <th>Nome Completo</th>
          <th>Email</th>
          <th>Serviço</th>
          <th>Telefone</th>
          <th>Data</th>
          <th>Hora</th>
          <th>Ações</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="agendamento in agendamentos" v-bind:key="agendamento.id">
          <td>{{agendamento.nome}}</td>
          <td>{{agendamento.email}}</td>
          <td>{{agendamento.servico}}</td>
          <td class="text-center">{{agendamento.telefone}}</td>
          <td class="text-right">{{agendamento.data}}</td>
          <td class="text-right">{{agendamento.hora}}</td>
          <td class="text-center">

            <a href="#" class="btn btn-sm btn-danger mx-1" title="Excluir">
              <i class="fas fa-minus-circle"></i>
            </a>
            <a href="#" class="btn btn-sm btn-info" title="Confirmar Agendamento" @click="destacar(carro.id)">
              <i class="far fa-star"></i>
            </a>
          </td>
        </tr>
      </tbody>
    </table>
  </div>
</template>

<script>
import axios from "axios";

export default {
  data() {
    return {
      agendamentos: []
    };
  },
  methods: {
    listar() {
      axios
        .get(this.$urlAPI + "/agendamentos")
        .then(response => (this.agendamentos = response.data));
  },
    goBack() {
      this.$router.push("/");
    }
  },

  mounted() {
    this.listar();
  },
  filters: {
    estiloMoeda(value) {
      return value.toLocaleString("pt-br", { minimumFractionDigits: 2 });
    }
  }
};
</script>

<style scoped>
table img {
  width: 100px;
  height: 60px;
}
</style>