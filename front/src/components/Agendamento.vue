<template>
  <div class="container">
    <h2>
      Agendamento de Horário
      <button class="btn btn-warning float-right" @click="goBack">
        <i class="fas fa-undo"></i> Voltar
      </button>
    </h2>
    <form @submit.prevent="salvar">
      <div class="row">
        <div class="col-sm-12">
          <div class="form-group">
            <label for="modelo">Nome Completo:</label>
            <input type="text" id="modelo" class="form-control" required v-model="agendamento.nome" ref="nome"/>
          </div>
        </div>
        <div class="col-sm-12">
          <div class="form-group">
            <label for="cor">Email:</label>
            <input type="text" id="email" class="form-control" required v-model="agendamento.email"/>
          </div>
        </div>
      </div>
      <div class="row">
        <div class="col-sm-6">
          <div class="form-group">
            <label for="servico_id">Serviços:</label>
            <select id="servico_id" class="form-control" required v-model="agendamento.servico_id">
              <option v-for="servico in servicos" :key="servico.id" :value="servico.id">{{servico.nome_servico}}</option>
            </select>
          </div>
        </div>
        <div class="col-sm-6">
          <div class="form-group">
            <label for="telefone">Telefone</label>
            <input type="text" id="telefone" class="form-control" required v-model="agendamento.telefone" />
          </div>
        </div>
      </div>
      <div class="row">
        <div class="col-sm-6">
          <div class="form-group">
            <label for="data">Data</label>
            <input type="text" id="data" class="form-control" required v-model="agendamento.data" />
          </div>
        </div>
        <div class="col-sm-6">
          <div class="form-group">
            <label for="foto">Hora</label>
            <input type="text" id="hora" class="form-control" required v-model="agendamento.hora" />
          </div>
        </div>
      </div>

      <button type="submit" class="btn btn-success px-4 mr-2">
        <i class="far fa-save"></i> Agendar
      </button>
      <button type="reset" class="btn btn-danger px-4">
        <i class="far fa-window-restore"></i> Limpar
      </button>
    </form>
  </div>
</template>

<script>
import axios from "axios";

export default {
  data() {
    return {
      agendamento: {
        id: null,
        nome: null,
        email: null,
        servico_id: null,
        telefone: null,
        data: null,
        hora: null,
      },
      servicos: null
    };
  },
  methods: {
    salvar() {
        axios
          .post(this.$urlAPI + "/agendamentos", this.agendamento)
          .then(response =>
            alert(`Horario Agendado Com Sucesso ${response.data}`)
          );
        this.agendamento = {};
        this.$refs.nome.focus();
      
    },
    goBack() {
      window.history.length > 1 ? this.$router.go(-1) : this.$router.push("/");
    }
  },
  mounted() {
    axios
      .get(this.$urlAPI + "/servicos")
      .then(response => (this.servicos = response.data));
  }
};
</script>

<style scoped>
</style>

