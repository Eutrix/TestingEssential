package dev.eutrix.badforgetemplate

import gg.essential.api.EssentialAPI
import net.minecraft.client.gui.GuiScreenBook
import net.minecraftforge.client.event.ClientChatReceivedEvent
import net.minecraftforge.client.event.GuiOpenEvent
import net.minecraftforge.common.MinecraftForge
import net.minecraftforge.fml.common.Mod
import net.minecraftforge.fml.common.event.FMLInitializationEvent
import net.minecraftforge.fml.common.event.FMLPreInitializationEvent
import net.minecraftforge.fml.common.eventhandler.SubscribeEvent

@Mod(name = "BadForgeTemplate",
     modid = "badforgemodid",
     version = "1.0.0", 
     modLanguageAdapter = "dev.eutrix.badforgetemplate.adapter.KotlinLanguageAdapter")

object BadForgeTemplate {
    @Mod.EventHandler
    fun onFMLInitialization(event: FMLInitializationEvent) {
        println("Goodbye, cruel world!")
} 
}
