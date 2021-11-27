package dev.eutrix.testingessential

import gg.essential.api.EssentialAPI
import net.minecraft.client.gui.GuiScreenBook
import net.minecraftforge.client.event.ClientChatReceivedEvent
import net.minecraftforge.client.event.GuiOpenEvent
import net.minecraftforge.common.MinecraftForge
import net.minecraftforge.fml.common.Mod
import net.minecraftforge.fml.common.event.FMLInitializationEvent
import net.minecraftforge.fml.common.event.FMLPreInitializationEvent
import net.minecraftforge.fml.common.eventhandler.SubscribeEvent

@Mod(name = "TestingEssential",
     modid = "essentialtest",
     version = "1.0.0", 
     modLanguageAdapter = "dev.eutrix.testingessential.adapter.KotlinLanguageAdapter")

object TestingEssential {
    @Mod.EventHandler
    fun onFMLInitialization(event: FMLInitializationEvent) {
        println("Goodbye, cruel world!")
} 
}
