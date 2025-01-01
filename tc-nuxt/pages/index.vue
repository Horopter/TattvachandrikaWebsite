<template>
  <div class="bg-amber-50 min-h-screen">
    <!-- Header -->
    <header class="bg-orange-50">
      <div class="container mx-auto flex justify-between items-center">
        <h1 class="text-xl font-bold text-orange-700">Hari Sarvottama</h1>
        <img
          src='../assets/images/Hanuma1.png'
          alt="hanuma"
        />
        <div class="relative flex flex-col items-center">
          <svg width="300" height="200">
            <defs>
              <path
                id="curve"
                d="M 150, 150 m -100, 0 a 100,100 0 1,1 200,0 a 100,100 0 1,1 -200,0"
              />
            </defs>
            <text>
              <textPath
                xlink:href="#curve"
                startOffset="25%"
                text-anchor="middle"
              >
                Sri Moola Gopala Krishno Vijayathe
              </textPath>
            </text>
          </svg>
          <img
            src='../assets/images/GopalaKrishna.png'
            alt="krishna"
            class="w-24 h-24 rounded-full absolute"
            style="top: 80px; left: 50%; transform: translateX(-50%)"
          />
        </div>
        <img
          src='../assets/images/hanuma2.png'
          alt="Bheema"
        />
        <h1 class="text-xl font-bold text-orange-700">Vaayu Jeevottama</h1>
      </div>
    </header>

    <!-- Institution Name -->
    <section class="text-orange-800 text-center py-4 bg-orange-100">
      <h2 class="text-2xl font-bold">
        Sri Jagadguru Sriman Madhvacharya Moola Maha Samsthanam
      </h2>
      <h3 class="text-xl">Sri Rajendratirthiya Poorvadi Matha</h3>
      <h3 class="font-bold text-2xl">Sri Vyasaraja Mutt (Sosale)</h3>
    </section>

    <!-- Main content -->
    <main class="container mx-auto mt-6 p-6">
      <div class="bg-white rounded-lg shadow-lg p-6 mt-4">
        <h2 class="text-3xl font-bold text-center mb-4 text-orange-800">
          Sri Tattvachandrika: Your Monthly Companion for Spiritual Growth and
          Knowledge
        </h2>

        <!-- Main image -->
        <div class="flex justify-center mb-6">
          <div class="relative">
            <img
              src="https://anandsp1.wordpress.com/wp-content/uploads/2020/08/moola-gopalakrishna-devaru-20.jpg"
              alt="Deity statue"
              class="rounded-lg shadow-md max-w-2xl"
            />
          </div>
        </div>

        <div class="p-4 bg-orange-100 text-center">
          <h1 class="text-xl font-sans font-semibold text-orange-900">Our Previous Editions</h1>
        </div>

        <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-6 mt-8">
          
          <!-- Card 1 -->
          <!-- <div class="rounded-lg shadow-md p-4 bg-orange-100">
            <img
              src="https://cdn.exoticindia.com/images/products/thumbnails/t800x600/books-2019/mzl307.jpg"
              alt="Book 1"
              class="w-full rounded-lg mb-4"
            />
            <p class="text-center text-orange-800 font-bold">January 2024</p>
          </div> -->

          <!-- Card 2 -->
          <div class="bg-orange-100 rounded-lg shadow-md p-4">
            <img
              src="assets\images\feb.jpg"
              alt="Book 2"
              class="w-full rounded-lg mb-4"
            />
            <p class="text-center text-orange-800 font-bold">February 2024</p>
          </div>

          <!-- Card 3 -->
          <div class="bg-orange-100 rounded-lg shadow-md p-4">
            <img
              src="assets\images\march.jpg"
              alt="Book 3"
              class="w-full rounded-lg mb-4"
            />
            <p class="text-center text-orange-800 font-bold">March 2024</p>
          </div>

          <!-- Card 4 -->
          <div class="bg-orange-100 rounded-lg shadow-md p-4">
            <img
              src="assets\images\april.jpg"
              alt="Book 4"
              class="w-full rounded-lg mb-4"
            />
            <p class="text-center text-orange-800 font-bold">April 2024</p>
          </div>

          <!-- Card 5 -->
          <div class="bg-orange-100 rounded-lg shadow-md p-4">
            <img
              src='E:\vyasaraja mutt\assets\images\may.jpg'
              alt="Book 6"
              class="w-full rounded-lg mb-4"
            />
            <p class="text-center text-orange-800 font-bold">May 2024</p>
          </div>

          <!-- Card 6 -->
          <div class="bg-orange-100 rounded-lg shadow-md p-4">
            <img
              src="assets\images\june.jpg"
              alt="Book 6"
              class="w-full rounded-lg mb-4"
            />
            <p class="text-center text-orange-800 font-bold">June 2024</p>
          </div>

          <!-- Card 7 -->
          <div class="bg-orange-100 rounded-lg shadow-md p-4">
            <img
              src='../assets/images/july.jpg'
              alt="Book 7"
              class="w-full rounded-lg mb-4"
            />
            <p class="text-center text-orange-800 font-bold">July 2024</p>
          </div>

          <!-- Card 8 -->
          <div class="bg-orange-100 rounded-lg shadow-md p-4">
            <img
              src="assets\images\august.jpg"
              alt="Book 8"
              class="w-full rounded-lg mb-4"
            />
            <p class="text-center text-orange-800 font-bold">August 2024</p>
          </div>
          <div class="bg-orange-100 rounded-lg shadow-md p-4">
            <img
              src="assets\images\september.jpg"
              alt="Book 8"
              class="w-full rounded-lg mb-4"
            />
            <p class="text-center text-orange-800 font-bold">September 2024</p>
          </div>
        </div>
        <div class="m-8 p-4 bg-orange-100">
          <h1 class="text-2xl font-semibold font-sans text-center text-orange-950">Want to be a subscriber to Sri Tattvachandrika Monthly Magazine of Sri Vyasaraja Mutt ? </h1>
          <h1 class="text-xl font-semibold font-sans underline text-red-500 text-center mt-5"><nuxt-link to="HomePage" target="_blank">Click Here</nuxt-link></h1> 
          
        </div>


        <!-- Mathas information -->
      </div>
    </main>
  </div>
</template>

<script>
export default {
  name: "LandingPage",
};
</script>

<style scoped>
svg text {
  font-size: 18px;
  font-weight: bold;
  fill: rgb(141, 12, 12);
}

header {
  padding: 10px 0;
}
</style>
