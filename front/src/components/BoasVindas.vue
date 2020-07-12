<template>
  <!--Carousel-->
  <div class="container-fluid">
    <div id="demo" class="carousel slide mb-5" data-ride="carousel">
      <ul class="carousel-indicators">
        <li data-target="#demo" data-slide-to="0" class="active"></li>
        <li data-target="#demo" data-slide-to="1"></li>
        <li data-target="#demo" data-slide-to="2"></li>
        <li data-target="#demo" data-slide-to="3"></li>
        <li data-target="#demo" data-slide-to="4"></li>
      </ul>
      <div class="carousel-inner">
        <div class="carousel-item active">
          <img src="capa.jpeg" alt="Capa" width="550" height="250" />
          <div class="carousel-caption">
            <h3>Agende seu Horário Por Aqui</h3>
            <p>Aqui você pode agendar seu horário com facilidade</p>
          </div>
        </div>
        <div class="carousel-item">
          <img src="corte.jpeg" alt="Corte" width="550" height="250" />
          <div class="carousel-caption">
            <h3>Corte de Cabelo</h3>
            <p>Com profissionais altamente treinados</p>
          </div>
        </div>
         <div class="carousel-item">
          <img src="pinturas.jpeg" alt="New York" width="550" height="250" />
          <div class="carousel-caption">
            <h3>Pinturas</h3>
            <p>Inclui mudança de cor total e luzes</p>
          </div>
        </div>
        <div class="carousel-item">
          <img src="maquiagem.jpeg" alt="Maqui" width="550" height="250" />
          <div class="carousel-caption">
            <h3>Maquiagem</h3>
            <p>Fique linda para sua festa</p>
          </div>
        </div>
       <div class="carousel-item">
          <img src="penteado.jpeg" alt="Pent" width="550" height="250" />
          <div class="carousel-caption">
            <h3>Penteado</h3>
            <p>Um lindo penteado para um momento espercial</p>
          </div>
        </div>
      </div>
      
      <a class="carousel-control-prev" href="#demo" data-slide="prev">
        <span class="carousel-control-prev-icon"></span>
      </a>
      <a class="carousel-control-next" href="#demo" data-slide="next">
        <span class="carousel-control-next-icon"></span>
      </a>
    </div>

<div class="container">
<div class="servis">
  <div class="servis items">
  <h2>Nossos Serviços</h2>
  <hr class="my-4">

    <div class="container mb-5">
      <div class="row">
        
        <div class="col-sm-4" v-for="servico in servicos" v-bind:key="servico.id">
          <div class="card mb-3">
            <h3 class="card-header card text-white bg-secondary">{{servico.nome_servico}}</h3>
            <img
              style="height: 200px; width: 100%; display: block;" v-bind:src="servico.foto" alt="Card image"/>
            <div class="card-body card-footer bg-secondary">
              <router-link to="/agendamentos">Agende por aqui</router-link>
            </div>
          </div>
        </div>
      </div>
        </div>
  </div>
</div>
</div>

        
  </div>
</template>



<script>
import axios from 'axios'

export default {
    data() {
        return {
            servs: [],
            servicos: [],
        }
    },
    components: {},
    mounted() {
        this.listar()

    },
    methods: {
        listar() {
            axios
              .get(this.$urlAPI+'/servicos')
              .then(response => (this.servicos = response.data))
        }
        },
    
    filters: {
        estiloMoeda(value) {
            return value.toLocaleString('pt-br', {minimumFractionDigits: 2})
        }
    }
}
</script>
<style>
body {
 background-color:#E5E5E5;
}
</style>

<style scoped>

img {
  width: 120px;
  height: 60px;
}
.carousel-inner img {
  width: 1500px;
  height: 550px;
}


</style>