<script lang="ts">
  import sleep from "../utils/sleep";
  export let text = "Loading...";

  let animated = true;

  const handleAnimationEnd = async () => {
    animated = false;
    await sleep(0);
    animated = true;
  };
</script>

<p class="text">
  {#each text.split("") as character, index}
    {#if character === " "}
      {" "}
    {:else}
      <span
        class="character"
        class:character--animated={animated}
        style="--delay: {index / 40}s;"
        on:animationend={index + 1 === text.length
          ? handleAnimationEnd
          : undefined}>{character}</span
      >
    {/if}
  {/each}
</p>

<style lang="scss" global>
  @keyframes bounce {
    0% {
      transform: translateY(0);
    }
    50% {
      transform: translateY(-40%);
    }
    100% {
      transform: translateY(0);
    }
  }

  .text {
    font-weight: bold;
    font-size: min(6vw, 1.5rem);
  }

  .character {
    display: inline-block;

    &--animated {
      animation: bounce 0.75s var(--delay) ease-in-out;
    }
  }
</style>
